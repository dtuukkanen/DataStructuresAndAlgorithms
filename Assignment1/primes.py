def primes(N):
    primes = 0
    for i in range(2, N + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes += 1
    return primes


if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15
