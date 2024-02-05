from collections import defaultdict


def main():
    students = defaultdict(int)
    N = int(input())
    for _ in range(N):
        students[input()] += 1
    stud_alphabetical = sorted(students.items(), key=lambda s: s[0])
    stud_probs = sorted(stud_alphabetical, key=lambda s: s[1], reverse=True)
    for s in stud_probs:
        print(s[0], s[1])


if __name__ == '__main__':
    main()
