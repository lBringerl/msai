import sys


for line in sys.stdin:
    _id, is_open, *hours = line.strip().split('\t')
    if _id is None:
        continue
    total = 0
    if is_open is None or is_open != '1':
        print(f'{_id}\t{total}')
        continue
    for v in hours:
        if v is None or v == '' or v == 'NULL' or v == 'null':
            continue
        try:
            start, end = v.split('-')
        except:
            continue
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
