import random

# Bilangan prima besar
FIELD = 2**521 - 1


# KONVERSI DATA

def text_to_number(msg):
    return int.from_bytes(msg.encode(), byteorder="big")

def number_to_text(num):
    size = (num.bit_length() + 7) // 8
    return num.to_bytes(size, byteorder="big").decode()


# PEMBENTUKAN SHARE

def create_shares(message, threshold, total_share):
    secret_num = text_to_number(message)

    # koefisien polinomial acak
    parameters = [secret_num] + [
        random.randint(1, FIELD - 1) for _ in range(threshold - 1)
    ]

    def evaluate(x):
        result = 0
        for power, coef in enumerate(parameters):
            result = (result + coef * pow(x, power, FIELD)) % FIELD
        return result

    return [(x, evaluate(x)) for x in range(1, total_share + 1)]

# REKONSTRUKSI SECRET

def reconstruct_secret(parts):
    def interpolate_zero(points):
        acc = 0
        for i, (xi, yi) in enumerate(points):
            basis = yi
            for j, (xj, _) in enumerate(points):
                if i != j:
                    inv = pow(xi - xj, -1, FIELD)
                    basis = (basis * (-xj) * inv) % FIELD
            acc = (acc + basis) % FIELD
        return acc

    secret_number = interpolate_zero(parts)
    return number_to_text(secret_number)


# EKSEKUSI PROGRAM

if __name__ == "__main__":
    pesan_rahasia = "KriptografiUPB2025"

    hasil_share = create_shares(pesan_rahasia, threshold=3, total_share=5)

    print("Shares:")
    for item in hasil_share:
        print(item)

    secret_kembali = reconstruct_secret(hasil_share[:3])
    print("\nRecovered secret:", secret_kembali)
