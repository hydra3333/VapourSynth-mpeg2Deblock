#!/usr/bin/env python3
"""S2-I3 P0 fixed allow-list, hashes, manifest verification and global verdict."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

EXPECTED = {
 'XP': ('LG_576i_1_XP', '4f3821b5086a98b6c1b9f36f1ad2fac187e3b852602b740d15ffd72ba162f127', 228, 720, 576, 1619),
 'XP_blocky': ('LG_576i_1_XP_blocky', '8d0326b5975b19b36742717a80be9eaf11bc21f379f2855eb22651e94dd16b20', 228, 720, 576, 25635),
 'SP': ('LG_576i_2_SP', '40a97ce1a9920cd63e45da13371e0b41ff1619fed688d6145899a300463cc5d9', 192, 720, 576, 1764),
 'SP_blocky': ('LG_576i_2_SP_blocky', '7e19ca6078075e7bf7a3a34bcda0816267e4d38ad02a56e01b6b0ed726ace746', 192, 720, 576, 19010),
 'LP': ('LG_576i_3_LP', '849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011', 204, 720, 576, 1533),
 'LP_blocky': ('LG_576i_3_LP_blocky', 'b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238', 204, 720, 576, 20300),
 '3A': ('TEST_3A_A002', '9a60a8d24a7e4a45cbe82b4f41d232ede0e5c00624e82a8f8099f61351957f33', 300, 704, 576, 8812),
 '3A_blocky': ('TEST_3A_A002_blocky', 'e6f556dd4aaed0f4709b7c011fcf045193dccbb8abd2a01c646dddf0da893c83', 300, 704, 576, 18190),
}
GENERATE = ('XP','XP_blocky','SP','SP_blocky','3A','3A_blocky')
PAIRS = ('XP','SP','LP','3A')


def sha256(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for buf in iter(lambda:f.read(1048576),b''):
            h.update(buf)
    return h.hexdigest()


def write_json(path, doc):
    target=Path(path)
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('w',encoding='ascii',newline='\n') as f:
        json.dump(doc,f,indent=2,sort_keys=True,allow_nan=False)
        f.write('\n')


def verify_index(label, path, out):
    from stage2_index_reader_v0_2 import read_index
    if label not in EXPECTED:
        raise ValueError('unknown or protected source label')
    stem, digest, n,w,h, count=EXPECTED[label]
    path=Path(path).resolve(strict=True)
    if path.name != stem+'.idx':
        raise ValueError('index basename and allow-listed source do not match')
    actual=sha256(path)
    if actual != digest:
        raise ValueError(f'{label} index SHA mismatch: {actual} expected {digest}')
    idx=read_index(path)
    if (idx.frame_count,idx.width,idx.height)!=(n,w,h):
        raise ValueError(f'{label} index geometry/frame count mismatch')
    seen=sum(1 for rec in idx.records if rec.picture_type=='P'
             for mb in rec.iter_macroblocks() if mb.coding==1)
    result={'label':label,'index_path':str(path),'index_sha256':actual,'frame_count':n,
            'width':w,'height':h,'P_skip_mb_count':seen,'P_skip_reference_count':count,
            'P_skip_count_matches_reference':seen==count,'status':'PASS'}
    if out:
        write_json(out,result)
    print(json.dumps(result,sort_keys=True))
    return 0


def check_admission(label, root):
    if label not in EXPECTED:
        raise ValueError('protected or unknown label')
    root=Path(root)
    try:
        obj=json.loads((root / label / 'pskip_identity.json').read_text(encoding='ascii'))
        meta=json.loads((root / label / 'source_manifest.json').read_text(encoding='ascii'))
        info=json.loads((root / label / 'index_validation.json').read_text(encoding='ascii'))
    except (OSError,KeyError,ValueError) as e:
        raise ValueError(f'{label}: incomplete/invalid admission evidence: {e}') from e
    if obj.get('schema')!='S2-I3-P0-PSKIP-1' or obj.get('status')!='REGISTERED':
        raise ValueError(f'{label}: exact P-skip registration not established')
    if obj.get('source_label')!=label or meta.get('label')!=label or info.get('label')!=label:
        raise ValueError(f'{label}: inconsistent evidence source label')
    stem, digest, frames,w,h,_ = EXPECTED[label]
    if meta.get('index_sha256')!=digest or obj.get('index_sha256')!=digest or info.get('index_sha256')!=digest:
        raise ValueError(f'{label}: admission index digest conflict')
    if (info.get('frame_count'),info.get('width'),info.get('height'))!=(frames,w,h):
        raise ValueError(f'{label}: index admission geometry conflict')
    index_path=Path(meta['index'])
    if not index_path.is_file() or index_path.name!=stem+'.idx' or sha256(index_path)!=digest:
        raise ValueError(f'{label}: actual admitted index file absent/changed')
    source_path=Path(meta['source'])
    if not source_path.is_file() or source_path.name!=stem+'.mpg' or sha256(source_path)!=meta.get('source_sha256') or obj.get('source_sha256')!=meta.get('source_sha256'):
        raise ValueError(f'{label}: source video missing/changed since admission')
    true=obj.get('true_position',{})
    if true.get('compared',0)<200 or true.get('compared')!=true.get('identical'):
        raise ValueError(f'{label}: true-position identity incomplete')
    if obj.get('picture_count_with_qualified_pskips',0)<10:
        raise ValueError(f'{label}: insufficient P picture observations')
    if len(obj.get('control_offsets',{}))!=24 or len(obj.get('temporal_controls',{}))!=3:
        raise ValueError(f'{label}: expected controls missing')
    for name,control in list(obj['control_offsets'].items())+list(obj['temporal_controls'].items()):
        if control.get('compared',0)<=0 or control.get('identical',0)>=control['compared']:
            raise ValueError(f'{label}: invalid/non-discriminating control {name}')
    return obj


def summarise(root):
    root=Path(root).resolve(strict=True)
    if not (root.parent / 'P0A_READY.txt').is_file():
        raise ValueError('P0A six-index regression marker absent')
    sources={}
    pairs={}
    diagnostics={}
    problems=[]
    for label in EXPECTED:
        try:
            pskip=check_admission(label,root)
            sources[label]='REGISTERED'
            manifest_path=root / label / 's2i2_diagnostics' / 'S2_I3_diagnostic_disposition.json'
            manifest=json.loads(manifest_path.read_text(encoding='ascii'))
            if manifest.get('label')!=label or manifest.get('not_a_P0_admission_gate') is not True:
                raise ValueError('diagnostic evidence mislabelled')
            diagnostics[label]='REPORTED_NOT_GATE'
        except (OSError,ValueError,KeyError,TypeError) as e:
            sources[label]='NOT_VERIFIED'
            diagnostics[label]='NOT_VERIFIED'
            problems.append(f'{label}: {type(e).__name__}: {str(e)[:120]}')
    for label in PAIRS:
        try:
            obj=json.loads((root/('PAIR_'+label)/'pair_correspondence.json').read_text(encoding='ascii'))
            if obj.get('schema')!='S2-I3-P0-PAIR-1' or obj.get('status') not in ('PASS','FAIL','INCONCLUSIVE'):
                raise ValueError('bad pair schema/status')
            if obj.get('group')!=label:
                raise ValueError('pair group label mismatch')
            orig=root / label / 'source_manifest.json'
            block=root / (label+'_blocky') / 'source_manifest.json'
            o=json.loads(orig.read_text(encoding='ascii'))
            b=json.loads(block.read_text(encoding='ascii'))
            if obj.get('original_sha256')!=o.get('source_sha256') or obj.get('blocky_sha256')!=b.get('source_sha256'):
                raise ValueError('pair media SHA mismatch with admission')
            pairs[label]=obj['status']
            if obj['status']!='PASS':problems.append(f'PAIR_{label}: {obj["status"]}')
        except (OSError,ValueError,KeyError,TypeError) as e:
            pairs[label]='MISSING_OR_INVALID'
            problems.append(f'PAIR_{label}: {type(e).__name__}: {str(e)[:120]}')
    ready=not problems
    doc={'schema':'S2-I3-P0-SUMMARY-1','sources':sources,'pairs':pairs,
         's2i2_diagnostics_only':diagnostics, 'READY_FOR_P1':ready,'problems':problems,
         'ready_is_numerical_only':True,
         'requires_owner_and_claude_gate_review':True}
    write_json(root/'P0_summary.json',doc)
    print(json.dumps(doc,indent=2,sort_keys=True))
    return 0 if ready else 2

def main():
    ap=argparse.ArgumentParser()
    sub=ap.add_subparsers(dest='task',required=True)
    a=sub.add_parser('verify-index'); a.add_argument('label',choices=tuple(EXPECTED));a.add_argument('path');a.add_argument('--out')
    b=sub.add_parser('summary');b.add_argument('root')
    d=sub.add_parser('check-admission');d.add_argument('label',choices=tuple(EXPECTED));d.add_argument('results_root')
    c=sub.add_parser('print-index-path');c.add_argument('label',choices=tuple(EXPECTED));c.add_argument('--extension',choices=('mpg','idx'),default='idx')
    args=ap.parse_args()
    try:
        if args.task=='verify-index':return verify_index(args.label,args.path,args.out)
        if args.task=='summary':return summarise(args.root)
        if args.task=='check-admission':
            check_admission(args.label,args.results_root)
            print('REGISTERED: '+args.label+' (evidence and actual source/index hashes validated)')
            return 0
        print(EXPECTED[args.label][0]+'.'+args.extension)
        return 0
    except (OSError,ValueError,RuntimeError) as e:
        print('P0 FAIL: '+str(e),file=sys.stderr)
        return 2
if __name__=='__main__':
    raise SystemExit(main())
