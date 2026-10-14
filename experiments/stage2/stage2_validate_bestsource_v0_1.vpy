import os
import sys

import vapoursynth as vs

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import stage2_index_reader_v0_1 as s2

core = vs.core
source_filename = globals().get("src")
index_filename = globals().get("idx")

if not source_filename or not index_filename:
    raise ValueError("S2-I1 requires --arg src=<source.mpg> and --arg idx=<matching.idx>")


def log(text=""):
    sys.stderr.write(f"--- [S2-I1] {text}\n")


def bestsource_picture_type(frame):
    if "_PictType" not in frame.props:
        raise ValueError("BestSource frame is missing _PictType")
    value = frame.props["_PictType"]
    if isinstance(value, (bytes, bytearray)):
        value = value.decode("ascii", "strict")
    return str(value)[:1]


log(f"source = {source_filename}")
log(f"index  = {index_filename}")
index = s2.read_index(index_filename)
clip = core.bs.VideoSource(source_filename)

clip_types = []
for n in range(clip.num_frames):
    clip_types.append(bestsource_picture_type(clip.get_frame(n)))

s2.validate_clip_metadata(
    index,
    frame_count=clip.num_frames,
    width=clip.width,
    height=clip.height,
    picture_types=clip_types,
)

summary = index.summary()
log(f"PASS records/frames = {index.frame_count}")
log(f"PASS dimensions     = {index.width}x{index.height}")
log(f"PASS picture types  = {summary['picture_types']}")
log(f"progressive_frame   = {summary['progressive_frame']}")
log(
    "leading B excluded from quality evidence = "
    f"{summary['leading_b_excluded_count']} ordinals={summary['leading_b_excluded_ordinals']}"
)
log("PASS BestSource/index structural and picture-type correspondence")
sys.stderr.flush()
clip.set_output()
