import os
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1494529336387178527/gRS3JMPBNUnsDgXyMNItYwN1iDpUBwCyyTY9G59tjWB3vn-J7AW9ohXFUe-n1JLgexiC"


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

    message = (
        f"Found {len(primes)} primes up to {number}.\n"
        f"Primes{primes}\n"
        f"Largest prime :{primes[-1]}"
    )

    requests.post(WEBHOOK_URL, json={"content": message})
