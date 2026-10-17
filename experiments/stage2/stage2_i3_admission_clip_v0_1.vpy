"""S2-I3 P0 BestSource admission; vspipe --arg label=... --arg src=... --arg idx=... --arg out=... --info."""
from __future__ import annotations
import functools
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
import vapoursynth as vs

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from stage2_index_reader_v0_2 import read_index,validate_clip_metadata
from stage2_i3_pskip_core_v0_1 import run_pskip, AdmissionStructureError
from stage2_i3_preflight_verdict_v0_1 import EXPECTED, sha256, write_json

label=globals().get('label')
src=globals().get('src')
idx_path=globals().get('idx')
out=globals().get('out')
if label not in EXPECTED or not all((src,idx_path,out)):
    raise ValueError('requires allow-listed --arg label, src, idx, out')
stem,expected_sha,expected_frames,w,h,reference_skips=EXPECTED[label]
if Path(src).name!=stem+'.mpg' or Path(idx_path).name!=stem+'.idx':
    raise ValueError('source/index basename does not match exact development allow-list')
actual_sha=sha256(idx_path)
if actual_sha!=expected_sha:
    raise ValueError(f'index SHA mismatch: {actual_sha}')
index=read_index(idx_path)
clip=vs.core.bs.VideoSource(src)
fmt=clip.format
if not fmt or fmt.color_family!=vs.YUV or fmt.sample_type!=vs.INTEGER or \
   fmt.bits_per_sample!=8 or fmt.subsampling_w!=1 or fmt.subsampling_h!=1:
    raise ValueError('BestSource must deliver unconverted planar 8-bit YUV420')

def get_type(n):
    value=clip.get_frame(n).props.get('_PictType')
    if value is None:raise ValueError(f'_PictType missing on frame {n}')
    if isinstance(value,(bytes,bytearray)):
        value=value.decode('ascii','strict')
    if str(value) not in ('I','P','B'):
        raise ValueError(f'invalid _PictType at frame {n}: {value!r}')
    return str(value)

# All ordinals, including leading B, undergo strict metadata validation.
clip_types=[get_type(n) for n in range(clip.num_frames)]
validate_clip_metadata(index,frame_count=clip.num_frames,width=clip.width,
                       height=clip.height,picture_types=clip_types)
if (clip.num_frames,clip.width,clip.height)!=(expected_frames,w,h):
    raise ValueError('unexpected allow-listed source frame count/geometry')

@functools.lru_cache(maxsize=8)
def get_y(n):
    fr=clip.get_frame(n)
    y=np.asarray(fr[0])  # native BestSource stride-aware plane-0 view
    y.setflags(write=False)
    if y.dtype!=np.dtype('uint8') or y.shape!=(h,w):
        raise ValueError(f'native plane-0 shape/dtype mismatch at {n}')
    return y

result=run_pskip(index,get_y)
result['source_label']=label
result['source_sha256']=sha256(src)
result['index_sha256']=actual_sha
result['expected_skip_count_info']=reference_skips
result['actual_index_skip_count_info']=sum(1 for r in index.records if r.picture_type=='P'
                                          for mb in r.iter_macroblocks() if mb.coding==1)
bs_path=Path(vs.core.bs.plugin_path).resolve()
if not bs_path.is_file():
    raise ValueError('BestSource plugin path cannot be verified')
result['runtime']={'python':sys.version,'numpy':np.__version__,
                   'vapoursynth':str(getattr(vs,'__version__','not exposed')),
                   'bestsource_plugin_path':str(bs_path),
                   'bestsource_plugin_sha256':sha256(bs_path),
                   'bestsource_plugin_version':str(getattr(vs.core.bs,'version','not exposed')),
                   'adapter_sha256':sha256(__file__)}
outdir=Path(out)
if outdir.name!=label:
    raise ValueError('output folder label mismatch (must be /<label>)')
write_json(outdir/'index_validation.json',{'label':label,'status':'PASS',
  'frame_count':index.frame_count,'width':index.width,'height':index.height,
  'index_sha256':actual_sha,'reader':'stage2_index_reader_v0_2',
  'picture_types_validated_all_frames':True})
write_json(outdir/'source_manifest.json',{'label':label,'source':str(Path(src).resolve()),
  'source_sha256':result['source_sha256'],'index':str(Path(idx_path).resolve()),
  'index_sha256':actual_sha,'runtime':result['runtime'],
  'kind':'Stage 2 development source; NOT hold-out'})
write_json(outdir/'pskip_identity.json',result)
sys.stderr.write(f'S2-I3 P-skip {label}: {result["status"]}, exact=' +
                 f'{result["true_position"]["identical"]}/{result["true_position"]["compared"]}, '
                 f'P pictures={result["picture_count_with_qualified_pskips"]}\n')
sys.stderr.flush()
if result['status']!='REGISTERED':
    raise RuntimeError('P0 admission did not REGISTER; see pskip_identity.json')
clip.set_output() # unchanged source; --info only; no filter or frame persistence
