"""CLAUDE-ONLY Linux-compatible rehearsal of exact pure-NumPy statistics code.

FFmpeg is NOT the owner's BestSource acceptance path. This never writes media.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
from stage2_index_reader_v0_2 import read_index, validate_clip_metadata
from stage2_registration_stats_v0_1 import RegistrationRun


def rehearse(src, idx, out):
    index = read_index(idx)
    w, h = index.width, index.height
    probe = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                            '-show_entries', 'frame=pict_type', '-of', 'json', src],
                           capture_output=True, text=True, check=True)
    types = [f.get('pict_type') for f in json.loads(probe.stdout).get('frames', [])]
    validate_clip_metadata(index, frame_count=len(types), width=w, height=h, picture_types=types)
    cmd = ['ffmpeg', '-v', 'error', '-i', src, '-map', '0:v:0', '-an', '-sn', '-dn',
           '-fps_mode', 'passthrough', '-pix_fmt', 'yuv420p', '-f', 'rawvideo', '-']
    pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    assert pipe.stdout is not None
    size = w * h * 3 // 2
    runner = RegistrationRun(index, out, src, 'FFmpeg rawvideo REHEARSAL ONLY',
                             'LP_blocky' if Path(src).stem.endswith('_blocky') else 'LP')
    for n in range(index.frame_count):
        frame = pipe.stdout.read(size)
        if len(frame) != size:
            pipe.kill()
            raise RuntimeError(f'FFmpeg premature EOF n={n}, bytes={len(frame)} expected={size}')
        y = np.frombuffer(frame[:w*h], dtype=np.uint8).reshape(h, w).astype(np.int16)
        runner.process(n, y)
        if (n + 1) % 25 == 0:
            print(f'REHEARSAL {n+1}/{index.frame_count}', flush=True)
    if pipe.stdout.read(1):
        pipe.kill()
        raise RuntimeError('FFmpeg unexpected extra decoded output frames')
    rc = pipe.wait()
    if rc:
        raise RuntimeError(f'FFmpeg decoder exit code {rc}')
    result = runner.finalise()
    print('REHEARSAL_ONLY', json.dumps(result, default=str))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('idx')
    parser.add_argument('out')
    args = parser.parse_args()
    try:
        rehearse(args.src, args.idx, args.out)
    except Exception as exc:
        print('REHEARSAL ERROR: ' + str(exc), file=sys.stderr)
        raise SystemExit(2)
