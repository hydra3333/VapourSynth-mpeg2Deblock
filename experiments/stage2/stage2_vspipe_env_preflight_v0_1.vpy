"""Import/plugin provenance check executed by the SAME vspipe as full analysis."""
import hashlib
import json
import os
from pathlib import Path
import sys
import numpy as np
import vapoursynth as vs

core = vs.core
bs = core.bs  # fail closed if plugin not loaded
if not callable(bs.VideoSource):
    raise RuntimeError('BestSource VideoSource not callable')
path = getattr(bs, 'plugin_path', None)
if not path or not Path(path).is_file():
    raise RuntimeError('cannot establish BestSource plugin file identity')
h = hashlib.sha256()
with open(path, 'rb') as handle:
    for chunk in iter(lambda: handle.read(1 << 20), b''):
        h.update(chunk)
info = {
    'python_executable': sys.executable,
    'python_version': sys.version,
    'numpy_version': np.__version__,
    'vapoursynth_version': str(getattr(vs, '__version__', 'not exposed')),
    'vapoursynth_core_version': str(getattr(core, 'version_string', 'not exposed')),
    'bestsource_plugin_path': str(Path(path).resolve()),
    'bestsource_plugin_sha256': h.hexdigest(),
    'bestsource_version': str(getattr(bs, 'version', 'not exposed')),
}
print('S2-I2 RUNTIME PREFLIGHT ' + json.dumps(info, sort_keys=True), file=sys.stderr)
# Execute deterministic unit tests in the actual vspipe Python environment.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from stage2_registration_tests_v0_1 import main as run_synthetic_tests
run_synthetic_tests()
# vspipe --info must see an output or it exits without completing a valid check.
core.std.BlankClip(width=16, height=16, length=1).set_output()
