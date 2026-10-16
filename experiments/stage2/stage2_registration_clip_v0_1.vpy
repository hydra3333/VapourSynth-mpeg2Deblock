"""S2-I2 BestSource frame adapter. Use vspipe --arg src=... --arg idx=... --arg out=... --info."""
from __future__ import annotations
import json
import hashlib
import os
import sys
from pathlib import Path

import numpy as np
import vapoursynth as vs

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from stage2_index_reader_v0_2 import read_index, validate_clip_metadata
from stage2_registration_stats_v0_1 import RegistrationRun

src, idx, output = (globals().get(key) for key in ('src', 'idx', 'out'))
if not all((src, idx, output)):
    raise ValueError('S2-I2 requires --arg src=<source> --arg idx=<index> --arg out=<scratch folder>')
index = read_index(idx)
clip = vs.core.bs.VideoSource(src)
if not clip.format or clip.format.color_family != vs.YUV or clip.format.sample_type != vs.INTEGER or \
   clip.format.bits_per_sample != 8 or clip.format.subsampling_w != 1 or clip.format.subsampling_h != 1:
    raise ValueError('S2-I2 requires native unmodified 8-bit YUV420P BestSource frames')


def picture_type(frame):
    value = frame.props.get('_PictType')
    if value is None:
        raise ValueError('BestSource frame missing _PictType')
    if isinstance(value, (bytes, bytearray)):
        value = value.decode('ascii', 'strict')
    return str(value)[0]

# Structural correspondence verifies every picture, even quality-excluded leading B.
clip_types = [picture_type(clip.get_frame(n)) for n in range(clip.num_frames)]
validate_clip_metadata(index, frame_count=clip.num_frames, width=clip.width,
                       height=clip.height, picture_types=clip_types)

bs = vs.core.bs
bs_path = Path(bs.plugin_path).resolve()
if not bs_path.is_file():
    raise ValueError('BestSource plugin path cannot be verified')
info = {'sys_executable': sys.executable, 'python': sys.version, 'numpy': np.__version__,
        'vapoursynth': str(getattr(vs, '__version__', 'not exposed')),
        'bestsource_plugin_path': str(bs_path),
        'bestsource_plugin_sha256': hashlib.sha256(bs_path.read_bytes()).hexdigest(),
        'bestsource_plugin_version': str(getattr(bs, 'version', 'not exposed')),
        'adapter_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
runner = RegistrationRun(index, output, src, 'BestSource / VapourSynth',
                         'LP_blocky' if Path(src).stem.endswith('_blocky') else 'LP',
                         runtime_info=info)
for n in range(clip.num_frames):
    frame = clip.get_frame(n)
    if n != 0 and picture_type(frame) != index.records[n].picture_type:
        raise ValueError(f'picture type changed at frame {n}')
    # NumPy sees VapourSynth's native plane-0 stride. The view is never mutated.
    view = np.asarray(frame[0])
    view.setflags(write=False)
    if view.shape != (clip.height, clip.width) or view.dtype != np.dtype('uint8'):
        raise ValueError('unsupported plane-0 native view format')
    runner.process(n, np.array(view, dtype=np.int16, copy=True))
    if (n + 1) % 25 == 0 or n + 1 == clip.num_frames:
        sys.stderr.write(f'S2-I2 processed {n+1}/{clip.num_frames}\n')
result = runner.finalise()
sys.stderr.write('S2-I2 completed: ' + json.dumps(result, allow_nan=True, default=str) + '\n')
sys.stderr.flush()
clip.set_output()
# Reports are written regardless of PASS/BLOCKED. Gate disposition is read from manifest by BAT.
