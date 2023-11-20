def get_dct(s1, s2):
    dct = {}
    for c1, c2 in zip(s1, s2):
        dct[c1] = c2
    if len(s1) > len(s2):
        dct.update({c: None for c in s1[len(s2):]})
    return dct


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(sorted(get_dct(s1, s2).items()))
