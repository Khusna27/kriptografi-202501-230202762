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
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
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
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit week11-secret-sharing
Author: Khusnatun Lina Fitri <husnatunlinafitri@gmail.com>
Date:   2025-12-19

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
