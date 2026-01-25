import hashlib
import time

# ==============================
# SIMULASI DATABASE MySpace
# Hash password TANPA SALT (lemah)
# ==============================
myspace_leaked_db = {
    "user_khusna": "5f4dcc3b5aa765d61d8327deb882cf99",  # password
    "user_atun": "e10adc3949ba59abbe56e057f20f883e",    # 123456
    "user_fitri": "25d55ad283aa400af464c76d713c07ad"    # 12345678
}

# ==============================
# FUNGSI LOAD DICTIONARY
# ==============================
def load_dictionary(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

# ==============================
# DICTIONARY ATTACK
# ==============================
def dictionary_attack(target_db, dictionary):
    print("=" * 55)
    print(" DICTIONARY ATTACK SIMULATION (MySpace Case) ")
    print("=" * 55)

    start_time = time.time()
    ditemukan = []

    for word in dictionary:
        word_hash = hashlib.md5(word.encode("utf-8")).hexdigest()

        for user, stolen_hash in target_db.items():
            if word_hash == stolen_hash:
                ditemukan.append((user, word))

    # ==============================
    # HASIL
    # ==============================
    print("\nHASIL PASSWORD YANG BERHASIL DITEMUKAN")
    print("-" * 55)
    print(f"{'User':<20} | {'Password Asli'}")
    print("-" * 55)

    for user, pwd in ditemukan:
        print(f"{user:<20} | {pwd}")

    print("-" * 55)
    print(f"Total password ditemukan : {len(ditemukan)}")
    print(f"Waktu eksekusi           : {time.time() - start_time:.4f} detik")
    print("=" * 55)

# ==============================
# EKSEKUSI UTAMA
# ==============================
if __name__ == "__main__":
    common_passwords = [
        "123456",
        "password",
        "qwerty",
        "admin",
        "12345678",
        "welcome"
    ]

    dictionary_attack(myspace_leaked_db, common_passwords)
