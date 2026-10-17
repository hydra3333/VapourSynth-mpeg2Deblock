"""S2-I3 P0 original/blocky temporal proof; output numerical JSON only."""
from pathlib import Path
import sys
import numpy as np
import vapoursynth as vs
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from stage2_i3_pair_correspondence_v0_1 import compare_pair
from stage2_i3_preflight_verdict_v0_1 import EXPECTED,PAIRS,sha256,write_json

label=globals().get('label')
original=globals().get('original')
blocky=globals().get('blocky')
out=globals().get('out')
if label not in PAIRS or not all((original,blocky,out)):
    raise ValueError('requires paired --arg label original blocky out')
for tag,src in ((label,original),(label+'_blocky',blocky)):
    if Path(src).name!=EXPECTED[tag][0]+'.mpg':
        raise ValueError('pair source basename not allowed')
if Path(out).name!='PAIR_'+label:
    raise ValueError('pair output dir must have PAIR_<label> name')
a=vs.core.bs.VideoSource(original)
b=vs.core.bs.VideoSource(blocky)
for clip,tag in ((a,'original'),(b,'blocky')):
    f=clip.format
    if not f or f.color_family!=vs.YUV or f.sample_type!=vs.INTEGER or f.bits_per_sample!=8 or \
       f.subsampling_h!=1 or f.subsampling_w!=1:
        raise ValueError(f'{tag}: expected native YUV420P8')
if (a.width,a.height)!=(b.width,b.height):
    raise ValueError('pair dimensions differ')
# All native display-order ordinals. Original/blocky MPEG-2 picture types may differ.
def y(clip,n):
    view=np.asarray(clip.get_frame(n)[0])
    view.setflags(write=False)
    return view
res=compare_pair(a.num_frames,b.num_frames,(a.height,a.width),
                 lambda n:y(a,n),lambda n:y(b,n))
res['group']=label
res['original_sha256']=sha256(original)
res['blocky_sha256']=sha256(blocky)
write_json(Path(out)/'pair_correspondence.json',res)
sys.stderr.write(f'S2-I3 PAIR {label}: {res["status"]}, decisive={res.get("decisive_frames",0)}\n')
sys.stderr.flush()
if res['status']!='PASS':
    raise RuntimeError('pair correspondence failed/blocked; inspect numerical report')
a.set_output()
