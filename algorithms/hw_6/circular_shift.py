def prefix_function(s):
    d = [0] * (len(s) + 1)
    for i in range(2, len(d)):
        d[i] = d[i - 1]
        while s[i - 1] != s[d[i]] and d[i] > 0:
            d[i] = d[d[i]]
        if s[i - 1] == s[d[i]]:
            d[i] += 1
    return d


def kmp(s, p):
    substrings = []
    d = prefix_function(f'{p}${s}')
    for i in range(len(p) + 1, len(d)):
        if len(p) == d[i]:
            substrings.append(i - 2 * len(p) - 1)
    return substrings


def main():
    s1 = input()
    s2 = input()
    if len(s1) != len(s2):
        return -1
    substrs = kmp(s1 * 2, s2)
    if substrs:
        return len(s1) - substrs[-1]
    else:
        return -1


if __name__ == '__main__':
    print(main())
