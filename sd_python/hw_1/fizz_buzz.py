
def get_fizz_buzz(num):
    if num % 15 == 0:
        return 'Fizz Buzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    return num


def fizz_buzz(n):
    inc = 1 if n > 1 else -1
    for i in range(1, n, inc):
        fb = get_fizz_buzz(i)
        print(f'{fb}, ', end='')
    fb = get_fizz_buzz(n)
    print(f'{fb}', end='')


if __name__ == '__main__':
    n = int(input())
    fizz_buzz(n)
