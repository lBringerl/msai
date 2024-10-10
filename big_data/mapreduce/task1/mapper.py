import json
import math
import sys


for line in sys.stdin:
    data = json.loads(line.strip())
    _id = data.get('business_id', None)
    if _id is None:
        continue
    total = 0
    is_open = data.get('is_open', None)
    if is_open is None or is_open != 1:
        print(f'{_id}\t{total}')
        continue
    hours = data.get('hours', None)
    if hours is None:
        print(f'{_id}\t{total}')
        continue
    for _, v in hours.items():
        start, end = v.split('-')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        if end_m == start_m == end_h == start_h == 0:
            continue
        if end_h < start_h:
            end_h += 24
        if end_m < start_m:
            mins = 60 - start_m + end_m
            sub_h = 1
        else:
            mins = end_m - start_m
            sub_h = 0
        total += (mins + (end_h - start_h - sub_h) * 60)
    print(f'{_id}\t{total}')
