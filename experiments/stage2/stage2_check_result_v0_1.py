"""Read registration gate JSON; descriptive weak signal never used as a failure criterion."""
import json
import sys
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: stage2_check_result_v0_1.py result_dir')
    p = Path(sys.argv[1]) / 'run_manifest.json'
    try:
        m = json.loads(p.read_text(encoding='utf-8'))
        print('S2-I2 ' + m['label'] + ' gate: ' + m['gate'])
        print('3x3=' + m['aligned']['shift'] + ' column=' + m['aligned']['column'] +
              ' row=' + m['aligned']['row'])
        if not m['known_bad_all_caught']:
            raise ValueError('known-bad control NOT caught')
        if m['gate'] != 'PASS':
            raise ValueError('registration not accepted: ' + m['gate'])
    except Exception as exc:
        print('ERROR: ' + str(exc), file=sys.stderr)
        raise SystemExit(2)
