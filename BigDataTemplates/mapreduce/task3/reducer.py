from collections import defaultdict
import sys


usefuls = defaultdict(list)
friends = defaultdict(int)


for line in sys.stdin:
    token, *data = line.strip().split('\t')
    if token == 'review':
        user_id, useful = data
        usefuls[user_id].append(int(useful))
    else:
        user_id, friends_data = data
        friends_number = len(friends_data.strip().split(', '))
        friends[user_id] = friends_number

for user in usefuls:
    usefuls[user].sort(reverse=True)
    top_usefuls = sum(usefuls[user][:5])
    friends_number = friends[user]
    print(f'{user}\t{top_usefuls}\t{friends_number}')
