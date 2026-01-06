# Laporan Praktikum Kriptografi
Minggu ke-: 11

Topik: 11 Secret Sharing (Shamir’s Secret Sharing)

Nama: Khusnatun Lina Fitri

NIM: 230202762

Kelas: 5IKRB

---

## 1. Tujuan
1. Menjelaskan konsep **Shamir Secret Sharing** (SSS).  
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.  
3. Menganalisis keamanan skema distribusi rahasia.  
---

## 2. Dasar Teori

Shamir Secret Sharing (SSS) adalah salah satu metode dalam kriptografi yang digunakan untuk membagi sebuah informasi rahasia ke dalam beberapa bagian yang disebut share, lalu dibagikan kepada beberapa pihak. Metode ini diperkenalkan oleh Adi Shamir dengan memanfaatkan konsep matematika polinomial. Dalam skema ini, sebuah rahasia dibagi menjadi sejumlah n share, namun rahasia tersebut hanya dapat dikembalikan jika minimal k share (threshold) dikumpulkan. Apabila jumlah share yang tersedia kurang dari nilai threshold, maka isi rahasia tidak dapat diketahui, sehingga tidak ada satu pihak pun yang memegang rahasia secara penuh.

Dalam proses simulasi pembagian rahasia menggunakan SSS, nilai rahasia terlebih dahulu dimasukkan sebagai konstanta pada sebuah polinomial dengan derajat k−1. Polinomial tersebut kemudian dihitung pada beberapa nilai tertentu untuk menghasilkan share yang berbeda-beda, yang selanjutnya dibagikan ke masing-masing pihak. Untuk mendapatkan kembali rahasia, diperlukan minimal k share yang digabungkan menggunakan metode interpolasi Lagrange. Melalui proses ini dapat dilihat bahwa satu share saja tidak cukup untuk mengungkap rahasia yang dibagi.

Dari aspek keamanan, Shamir Secret Sharing memiliki kelebihan karena tingkat keamanannya tidak bergantung pada kemampuan komputasi pihak penyerang. Pihak yang hanya memiliki share di bawah batas threshold tidak akan memperoleh informasi apa pun mengenai rahasia utama. Oleh karena itu, skema ini banyak diterapkan pada sistem yang membutuhkan pengamanan tinggi, seperti pengelolaan kunci kriptografi, sistem kontrol bersama, dan penyimpanan data penting. Dengan mekanisme tersebut, SSS menjadi solusi yang cukup efektif untuk distribusi rahasia secara aman dan terkontrol.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code 
- Git dan akun GitHub  
- Google Chrome

---

## 4. Langkah Percobaan
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code

### Langkah 1 - Implementasi Shamir Secret Sharing
```
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
```

Hasilnya :

```
Shares:
(1, 5252622653081142092705565569753049476834747109407576647937036046869138840364209310422762487312824717474209386886353595980127215440311349170301700024574251315)
(2, 2067633841857468654787552642803085126749270601313001909292886968024591909069543816084115079174244034970537488719350581380709932374647778938207609727201869425)  
(3, 4174628886590199116209762817312893384282441076002886602856479681837445572911315621229177056907167062443576928281959244629779676199353272086180935214957394413)  
(4, 4708810127148723761990295294201081032164823233333925319233350729122156648491868673735388779850139244916031394182698727690214458914711184801647648196725769128)  
(5, 3670177563533042592129150073467648070396417073306118058423500109878725135811202973602750248003160582387900886421569030562014280520721517084607748672506993570)  

Recovered secret: KriptografiUPB2025
```

### Langkah 2 - Simulasi Manual (Tanpa Library)

```
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
```

Hasilnya : 
```
Shares:
(1, 1413)
(2, 1277)
(3, 826)
(4, 60)
(5, 1068)

Recovered Secret: 1234
```
### Langkah 3 - Analisis Keamanan

1. Mengapa skema (k, n) aman meskipun sebagian share bocor?

   Skema Shamir’s Secret Sharing (k, n) dikembangkan untuk menjamin kerahasiaan data meskipun sebagian share diketahui oleh pihak yang tidak berhak. Mekanisme keamanan pada skema ini menggunakan polinomial berderajat (k−1) yang didefinisikan pada medan hingga.

    Apabila jumlah share yang dimiliki belum mencapai nilai threshold k, maka proses rekonstruksi secret tidak     dapat dilakukan. Hal ini disebabkan karena data yang tersedia belum cukup untuk menentukan satu polinomial secara unik, sehingga nilai secret tidak dapat diketahui. Dengan demikian, skema ini tetap aman walaupun terjadi kebocoran sebagian share.

2.  Apa risiko jika threshold k terlalu kecil atau terlalu besar?

    Penentuan nilai threshold k memiliki pengaruh langsung terhadap tingkat keamanan dan keandalan sistem.

    Jika nilai k ditetapkan terlalu kecil, maka secret dapat dipulihkan dengan jumlah share yang sedikit, sehingga meningkatkan risiko kebocoran apabila share tersebut jatuh ke pihak yang tidak berwenang.

    Sebaliknya, apabila nilai k terlalu besar, maka proses pemulihan secret menjadi lebih sulit. Kehilangan satu atau beberapa share dapat mengakibatkan secret tidak dapat direkonstruksi kembali. Oleh karena itu, pemilihan nilai threshold k harus disesuaikan agar tercapai keseimbangan antara aspek keamanan dan ketersediaan data.

3. Bagaimana penerapan SSS di dunia nyata (contoh: manajemen kunci cryptocurrency, recovery password)?

    Skema Shamir’s Secret Sharing telah banyak dimanfaatkan dalam berbagai bidang keamanan informasi. Salah satu penerapannya adalah pada pengelolaan kunci kriptografi, seperti kunci privat pada sistem cryptocurrency, di mana kunci dibagi menjadi beberapa share untuk menghindari penyimpanan terpusat.

    Selain itu, metode ini juga digunakan pada sistem pemulihan password dan perlindungan data sensitif, sehingga pemulihan hanya dapat dilakukan melalui kerja sama beberapa pihak terpercaya. Dalam lingkungan organisasi, skema ini diterapkan untuk meningkatkan keamanan akses terhadap sistem penting dan mengurangi risiko penyalahgunaan wewenang.


Sehingga dapat diismpulkan bahwa keamanan pada Shamir's Secret Sharing memberikan tingkat keamanan yang tinggi terhadap perlindungan secret. Kerahasiaan data tetap terjaga selama jumlah share yang tersedia belum memenuhi nilai threshold k. Penentuan nilai k yang tetap menjadi faktor penting supaya sistem tetap aman sekaligus dapat diandalkan.

---

## 6. Hasil dan Pembahasan
- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

1. Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?  
2. Apa peran **threshold (k)** dalam keamanan secret sharing?  
3. Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat.

Jawaban : 

1. Keuntungan utama Shamir Secret Sharing dibandingkan pembagian kunci secara langsung terletak pada tingkat keamanannya. Jika kunci dibagikan secara langsung, setiap pihak memiliki salinan kunci yang sama, sehingga kebocoran pada satu pihak saja sudah cukup untuk membahayakan seluruh sistem. Berbeda dengan Shamir Secret Sharing, di mana kunci dibagi menjadi beberapa bagian yang masing-masing tidak memiliki arti jika berdiri sendiri. Selama jumlah bagian yang bocor belum mencapai batas tertentu, rahasia utama tetap aman.

2. Threshold (k) berfungsi sebagai penentu jumlah minimal bagian rahasia yang harus digabungkan agar rahasia dapat dikembalikan. Nilai ini sangat berpengaruh terhadap keamanan karena pihak yang memiliki bagian di bawah batas threshold tidak akan bisa mengetahui isi rahasia. Semakin besar nilai threshold yang ditetapkan, maka semakin sulit bagi pihak yang tidak berwenang untuk mengakses rahasia tersebut. Namun, nilai ini juga perlu disesuaikan agar proses pemulihan rahasia tetap memungkinkan ketika dibutuhkan.

3. Contoh penerapan Shamir Secret Sharing dalam kehidupan nyata dapat ditemukan pada pengelolaan kunci penting di sebuah organisasi. Misalnya, kunci utama sistem dibagi kepada beberapa administrator, dan kunci tersebut hanya dapat digunakan jika sejumlah administrator tertentu bekerja sama. Dengan cara ini, tidak ada satu orang pun yang memiliki kendali penuh terhadap kunci penting, sehingga risiko penyalahgunaan atau kehilangan kunci dapat dikurangi.
---

## 8. Kesimpulan

    Berdasarkan hasil praktikum, metode Shamir’s Secret Sharing berhasil membagi secret menjadi beberapa share tanpa mengungkapkan isi secret secara langsung. Secret hanya dapat dikembalikan jika jumlah share yang digunakan memenuhi nilai threshold yang ditentukan. Hal ini menunjukkan bahwa metode ini efektif dalam menjaga keamanan data rahasia.

---

## 9. Daftar Pustaka

---

## 10. Commit Log

```
commit week11-secret-sharing
Author: Khusnatun Lina Fitri <husnatunlinafitri@gmail.com>
Date:   2025-12-19

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
