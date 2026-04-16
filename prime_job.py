import os


def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


if __name__ == "__main__":
    number = int(os.environ.get("NUMBER", 100))
    print(f"Finding primes up to {number}...")
    primes = find_primes(number)
    print(f"Found {len(primes)} primes: {primes}")
