"""S2-I3 source-labelled reuse of S2-I2 numerical diagnostics; NEVER admission gate."""
from pathlib import Path
import json
import sys
import numpy as np
import vapoursynth as vs
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from stage2_index_reader_v0_2 import read_index,validate_clip_metadata
from stage2_i3_preflight_verdict_v0_1 import EXPECTED,sha256,write_json
from stage2_registration_stats_v0_1 import RegistrationRun
label=globals().get('label')
src=globals().get('src')
idx=globals().get('idx')
out=globals().get('out')
if label not in EXPECTED or not all((src,idx,out)):
    raise ValueError('diagnostic requires allow-listed label/src/idx/out')
stem,expected_sha,frames,w,h,_=EXPECTED[label]
if Path(src).name!=stem+'.mpg' or Path(idx).name!=stem+'.idx' or Path(out).name!=label:
    raise ValueError('invalid diagnostic source/index/out association')
if sha256(idx)!=expected_sha:
    raise ValueError('diagnostic actual index digest mismatch')
index=read_index(idx)
clip=vs.core.bs.VideoSource(src)
f=clip.format
if not f or f.color_family!=vs.YUV or f.sample_type!=vs.INTEGER or f.bits_per_sample!=8 or f.subsampling_w!=1 or f.subsampling_h!=1:
    raise ValueError('diagnostic requires unconverted YUV420P8')

def picture_type(fr):
    val=fr.props.get('_PictType')
    if val is None:raise ValueError('missing _PictType')
    if isinstance(val,(bytes,bytearray)):val=val.decode('ascii','strict')
    return str(val)
validate_clip_metadata(index,frame_count=clip.num_frames,width=clip.width,height=clip.height,
                       picture_types=(picture_type(clip.get_frame(n)) for n in range(clip.num_frames)))
runner=RegistrationRun(index,Path(out)/'s2i2_diagnostics',src,'BestSource / VapourSynth',label)
for n in range(clip.num_frames):
    frame=clip.get_frame(n)
    if picture_type(frame)!=index.records[n].picture_type:
        raise ValueError(f'picture type mismatch at {n}')
    view=np.asarray(frame[0]);view.setflags(write=False)
    if view.shape!=(h,w) or view.dtype!=np.dtype('uint8'):
        raise ValueError('unexpected luma format')
    runner.process(n,np.array(view,dtype=np.int16,copy=True))
    if (n+1)%25==0 or n+1==clip.num_frames:
        sys.stderr.write(f'S2-I3 diagnostic {label}: {n+1}/{clip.num_frames}\n')
old=runner.finalise()
write_json(Path(out)/'s2i2_diagnostics'/'S2_I3_diagnostic_disposition.json',{
    'label':label,'name':'Original-threshold S2-I2 diagnostic, NOT registration admission',
    'old_gate_as_reported_only':str(old.get('gate','unknown')),
    'not_a_P0_admission_gate':True,
    'result_summary':str(old)[:1000]})
sys.stderr.write(f'S2-I3 S2-I2 diagnostics {label}: reports written, no admission verdict\n')
sys.stderr.flush()
clip.set_output()
