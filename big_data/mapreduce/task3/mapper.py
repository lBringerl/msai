import json
import math
import os
import sys


filename = os.environ['mapreduce_map_input_file']

for line in sys.stdin:
    data = json.loads(line.strip())
    if 'review' in filename:
        token = 'review'
        try:
            user_id = data['user_id']
            useful = data['useful']
        except:
            continue
        print(f'{token}\t{user_id}\t{useful}')
    else:
        token = 'user'
        try:
            user_id = data['user_id']
            friends = data['friends']
        except:
            continue
        print(f'{token}\t{user_id}\t{friends}')
