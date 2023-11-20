def is_prime(num, prev_primes):
    for p in prev_primes:
        if num % p == 0:
            return False
    return True


def gen_prime():
    yield 1
    primes = []
    cnt = 2
    while 1:
        if is_prime(cnt, primes):
            primes.append(cnt)
            yield cnt
        cnt += 1


if __name__ == '__main__':
    i = int(input())
    prime_g = gen_prime()
    for i in range(i + 1):
        prime = next(prime_g)
    print(prime)
