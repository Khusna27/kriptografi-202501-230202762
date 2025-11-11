# Laporan Praktikum Kriptografi
Minggu ke-: 7 
Topik: Diffie-Hellman Key Exchange
Nama: Khusnatun Lina Fitri
NIM: 230202762 
Kelas: 5IKRB

---

## 1. Tujuan
1. Melakukan simulasi protokol **Diffie-Hellman** untuk pertukaran kunci publik.  
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.  
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan **Man-in-the-Middle / MITM**).  

---

## 2. Dasar Teori
Protokol Diffie-Hellman Key Exchange adalah salah satu metode kriptografi paling awal yang memungkinkan dua pihak untuk membangun kunci rahasia bersama melalui saluran komunikasi publik tanpa perlu mengirimkan kunci itu secara langsung. Prinsip kerja Diffie-Hellman berdasarkan pada masalah logaritma diskrit, yaitu kesulitan menghitung nilai eksponen rahasia dari hasil perpangkatan modular, sehingga kunci publik dapat diketahui dan kunci privat tetap aman.

Dalam prosesnya, kedua pihak menyepakati dua bilangan publik yaitu bilangan prima besar 𝑝 dan generator 𝑔. Masing-masing pihak

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
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?  
2. Apa kelemahan utama protokol Diffie-Hellman murni?  
3. Bagaimana cara mencegah serangan MITM pada protokol ini?

Jawaban : 
1. Karena protokol Diffie-Hellman menggunakan konsep matematika eksponensial modular yang membuat pihak ketiga sulit menghitung kunci rahasia bersamaa (shared key) meskipun semua nilai yang dikirim lewat jaringan yang diketahui publik.

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
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
