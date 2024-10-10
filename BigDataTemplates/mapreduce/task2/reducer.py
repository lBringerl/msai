import sys


for line in sys.stdin:
    left, right = line.strip().split('\t')
    print(f'{right}\t{left}')
