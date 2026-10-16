"""Independent S2-I1 reader check for the S2-I2 scratch LP_blocky index."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from stage2_index_reader_v0_2 import read_index
import hashlib

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

EXPECTED = 'b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238'

def main(path):
    if sha256(path) != EXPECTED:
        raise ValueError('LP_blocky index SHA-256 mismatch (expected ' + EXPECTED + ')')
    s = read_index(path)
    d = s.summary()
    checks = {
        'record_count': 204,
        'dimensions': [720, 576],
        'mb_grid': [45, 36],
        'picture_types': {'B': 135, 'I': 19, 'P': 50},
        'picture_structures': {'3': 204},
        'progressive_frame': {'0': 204},
        'transform_states': {'FIELD':33853, 'FRAME':54292, 'NONE':242335},
        'qp_histogram': {'62':330480},
        'leading_b_excluded_count': 0,
        'leading_b_excluded_ordinals': [],
    }
    for name, expected in checks.items():
        if d[name] != expected:
            raise ValueError(f'LP_blocky {name} mismatch: {d[name]!r}, expected {expected!r}')
    if s.records[0].picture_type != 'I':
        raise ValueError('LP_blocky leading picture must be I')
    print('PASS: S2-I2 LP_blocky independent SHA-256 and structural identity match')
    print('SHA-256=' + EXPECTED)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python stage2_validate_lp_blocky_v0_1.py INDEX')
    try:
        main(sys.argv[1])
    except Exception as exc:
        print('ERROR: ' + str(exc), file=sys.stderr)
        raise SystemExit(2)
