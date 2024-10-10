import sys


businesses = []


for line in sys.stdin:
    left, right = line.strip().split('\t')
    businesses.append((right, left))


for business in businesses:
    print(f'{business[0]}\t{business[1]}')
