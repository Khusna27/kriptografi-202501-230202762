# Laporan Praktikum Kriptografi

Minggu ke-: 14

Topik: Analisis Serangan Kriptografi

Nama: Khusnatun Lina Fitri

NIM: 230202762

Kelas: 5IKRB

---

## 1. Tujuan

1. Mengidentifikasi jenis serangan pada sistem informasi nyata.  
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.  
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori

Kriptografi merupakan teknik yang digunakan untuk mengamankan data agar tidak dapat dibaca oleh pihak yang tidak berwenang. Dalam sistem komputer dan jaringan, kriptografi berperan penting untuk menjaga kerahasiaan dan keamanan informasi, seperti data login, pesan, dan transaksi digital. Namun, meskipun suatu sistem sudah menggunakan algotirma kriptografi, sistem tersebut tetap berpotensi mengalami serangan jika memiliki kelemahan, baik dari sisi algoritma maupun cara penerapannya.

Analisis serangan kriptografi digunakan untuk mempelajari dan menguji bagaimana suatu sistem kriptografi dapat diserang atau ditembus oleh pihak yang tidak berhak. Salah satu contoh serangan yang sering terjadi adalah brute force attack, yaitu serangan dengan cara mencoba semua kemungkinan kunci atau password sampai menemukan yang benar. Selain itu, terdapat juga jenis serangan lain seperti known-plaintext attack dan ciphertext-only attack yang memanfaatkan informasi tertentu untuk memecahkan sistem keamanan.

Dengan melakukan analisis serangan kriptografi , pengembang dapat mengetahui kelemahan pada sistem keamanan yang digunakan. Hasil dari analisis ini dapat dijadikan sebagai bahan evaluasi untuk meningkatkan keamanan, seperti menggunakan algoritma yang lebih kuat, memperpanjang kunci enkripsi, dan menerapkan sistem keaman tambahan. Oleh karena itu, analisis serangan kriptpgrafi sangat penting untuk memastikan data tetap aman dari berbagai ancaman keamanan digital.

---

## 3. Alat dan Bahan
- Python 3.12.2  
- Visual Studio Code   
- Git dan akun GitHub  
- Library Python hashlib
- File dicyionary password 

---

## 4. Langkah Percobaan

1. Membuat file `my_space_simulasi.py` di folder `praktikum/week14-analisis serangan/src/`.
2. Menulis kode Python untuk mensimulasikan penyimpanan password MySpace menggunakan algoritma hash MD5 tanpa salt.
3.Membuat file teks dictionary.txt yang berisi kumpulan password umum seperti 123456, password, qwerty, dan 12345678.
4. Mengimplementasikan fungsi dictionary attack untuk mencocokkan hash MD5 hasil kebocoran dengan daftar password pada file dictionary.txt.
5. Menjalankan program melalui terminal menggunakan perintah python my_space_simulasi.py.
6. Mencatat hasil keluaran (output) ketika password berhasil ditemukan melalui proses dictionary attack.
7. Membuat folder screenshot di `praktikum/week14-analisis serangan' untuk meng aploud hasil kode yang telah dijalankan.

---

## 5. Source Code
```
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
```

Hasilnya : 
```
=======================================================
 DICTIONARY ATTACK SIMULATION (MySpace Case) 
=======================================================

HASIL PASSWORD YANG BERHASIL DITEMUKAN
-------------------------------------------------------
User                 | Password Asli
-------------------------------------------------------
user_atun            | 123456
user_khusna          | password
user_fitri           | 12345678
-------------------------------------------------------
Total password ditemukan : 3
Waktu eksekusi           : 0.0049 detik
=======================================================
```
---

## 6. Hasil dan Pembahasan

Hasil eksekusi program my_space_simulasi.py : 

![Hasil Eksekusi](screenshots/hasilmyspace.PNG)

Hasil dan Pembahasan : 

MySpace mengalami kebocoran data besar yang terungkap sekitar tahun 2016, di mana ratusan juta akun pengguna bocor ke publik. Data yang bocor berisi hash password yang sebagian besar disimpan tanpa salt dan menggunakan algoritma hash yang cepat dihitung. Kondisi ini memungkinkan penyerang melakukan offline password cracking tanpa batasan percobaan.

Jenis serangan yang digunakan adalah dictionary attack dan brute force attack. Vektor serangan berasal dari kebocoran database hash password MySpace, sehingga penyerang dapat mencocokkan hash secara offline menggunakan berbagai kombinasi password umum.

erdasarkan hasil simulasi yang dilakukan menggunakan kode Python, seluruh akun pada database simulasi berhasil ditemukan password aslinya dalam waktu yang relatif singkat. Hasil ini menunjukkan bahwa penggunaan algoritma hash yang cepat tanpa salt sangat rentan terhadap serangan dictionary attack, terutama jika pengguna menggunakan password yang sederhana dan umum.

Kelemahan utama pada sistem terletak pada pemilihan algoritma kriptografi yang tidak dikhususkan untuk pengamanan password serta tidak adanya penerapan salt pada proses hashing. Selain itu, tidak terdapat mekanisme perlindungan tambahan setelah terjadinya kebocoran data. Oleh karena itu, kasus MySpace membuktikan bahwa permasalahan keamanan lebih disebabkan oleh kelemahan algoritma dan implementasi sistem, bukan hanya kesalahan dari sisi pengguna.

---

## 7. Jawaban Pertanyaan
1. Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?  
2. Apa bedanya kelemahan algoritma dengan kelemahan implementasi?  
3. Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?

Jawaban : 

1. Banyak sistem lama masih rentang terhadap serangan brute force atau dictionary attack karena menggunakan algoritma kriptografi yang sudah lama atau yang panjang kuncinya masih pendek. Selain itu, sistem lama juga sering menyimpan password tanpa teknik pengamanan tambahan seperti hashing yang kuat. Faktor lain yang mempengaruhi yaitu keterbatasan teknologi pada saat sistem tersebut dibuat, sehingga tidak dirancang untuk menghadapi kemampuan komputasi yang semakin kuat saat ini.

2. Perbedaan antara kelemahan algoritma dengan kelemahan implementasi yaitu kelemahan algoritma terjadi ketika algoritma kriptografi itu sendiri sudah tidak aman, misalnya karena memiliki celah matematis atau sudah berhasil dipecahkan. Sedangkan kelemahan implementasi terjadi bukan karena algoritmanya, tetapi karena kesalahhan dalam penerapannya, seperti penggunaan kunci yang lemah, penyimpanan password yang tidak aman atau konfigurasi sistem yang salah.

3. Organisasi dapat memastikan keamanan sistem kroptografi dengan cara selalu memperbarui algoritma dan standar keamanan yang digunakan sesuai perkembangan teknologi. Selain itu, perlu dilakukan pengujian keamanan secara berkala, seperti penetration testing dan audit sistem. Organisasi juga harus menerapkan praktik keamanan yang baik, seperti manajemen kunci yang benar dan edukasi keamanan bagi pengelola sistem.
---

## 8. Kesimpulan

Praktikum ini menunjukkan bahwa penyimpanan password menggunakan hash tanpa salt dan algoritma yang cepat sangat tidak aman, karena memungkinkan penyerang melakukan pemecahan password secara offline dengan mudah. Kasus MySpace membuktikan bahwa kelemahan utama terletak pada desain dan implementasi sistem keamanan, bukan hanya pada pengguna.

Untuk mencegah kasus seperti MySpace, sistem sebaiknya menggunakan algoritma hashing khusus password seperti bcrypt, scrypt, atau Argon2 dengan penerapan salt pada setiap password. Selain itu, diperlukan kebijakan password yang kuat dan peningkatan keamanan sistem agar risiko kebocoran data dapat diminimalkan.

---

## 9. Daftar Pustaka


---

## 10. Commit Log

```
week14-analisis-serangan
Author: Khusnatun Lina Fitri <husnatunlinafitri@gmail.com>
Date:   2026-01-25

   week14-analisis-serangan : Analisis Serangan Kriptografi
```
