import random

PRIME = 2089  # bilangan prima (harus > secret)

# Membuat polinomial derajat k-1
def generate_polynomial(secret, k):
    coeffs = [secret]
    for _ in range(k - 1):
        coeffs.append(random.randint(1, PRIME - 1))
    return coeffs

# Evaluasi polinomial
def evaluate_polynomial(coeffs, x):
    result = 0
    for power, coef in enumerate(coeffs):
        result = (result + coef * pow(x, power)) % PRIME
    return result

# Membagi rahasia menjadi n shares
def split_secret(secret, k, n):
    coeffs = generate_polynomial(secret, k)
    shares = []
    for i in range(1, n + 1):
        shares.append((i, evaluate_polynomial(coeffs, i)))
    return shares

# Rekonstruksi rahasia (Lagrange)
def recover_secret(shares):
    secret = 0
    for i, (xi, yi) in enumerate(shares):
        li = 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                li *= (-xj) * pow(xi - xj, -1, PRIME)
                li %= PRIME
        secret += yi * li
        secret %= PRIME
    return secret


# ================== MAIN PROGRAM ==================
secret = 1234  # rahasia (angka)
k = 3          # threshold
n = 5          # jumlah share

shares = split_secret(secret, k, n)

print("Shares:")
for s in shares:
    print(s)

recovered = recover_secret(shares[:3])
print("\nRecovered Secret:", recovered)
