from flask import Flask, render_template , request


app = Flask(__name__)


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


@app.route("/", methods=["GET", "POST"])
def home():
    primes = []

    if request.method == "POST":
        number = int(request.form["number"])
        primes = find_primes(number)

    return render_template("index.html", primes=primes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

