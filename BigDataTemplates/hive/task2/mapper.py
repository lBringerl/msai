from collections import defaultdict
import json
import sys


result_dct = defaultdict(int)
for line in sys.stdin:
    attributes = line.strip()
    dct_attrs = json.loads(attributes)
    for k, v in dct_attrs.items():
        if v[0] == '{':
            inner_dct = eval(v)
            for inner_k, inner_v in inner_dct.items():
                result_dct[f'{k}:{inner_k}:{inner_v}'] += 1
        else:
            result_dct[f'{k}:{v}'] += 1

for k, v in result_dct.items():
    print(f'{k}\t{v}')
