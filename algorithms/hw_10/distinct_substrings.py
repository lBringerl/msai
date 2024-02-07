p = 10000000000000061
a = 321


def c_to_i(ch):
    return ord(ch) - ord('a') + 1


def distinct_substrings(s):
    N = len(s)
    a_pow = [1] * (N + 1)
    for i in range(N):
        a_pow[i + 1] = (a_pow[i] * a) % p
    hashes = set()
    for i in range(N):
        h = 0
        for j in range(i, N):
            h = (h + c_to_i(s[j]) * a_pow[j - i]) % p
            hashes.add(h)
    return len(hashes)


if __name__ == '__main__':
    s = input().strip()
    print(distinct_substrings(s))
