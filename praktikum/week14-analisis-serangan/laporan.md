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
1. Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?  
2. Apa bedanya kelemahan algoritma dengan kelemahan implementasi?  
3. Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?

Jawaban : 

1. Banyak sistem lama masih rentang terhadap serangan brute force atau dictionary attack karena menggunakan algoritma kriptografi yang sudah lama atau yang panjang kuncinya masih pendek. Selain itu, sistem lama juga sering menyimpan password tanpa teknik pengamanan tambahan seperti hashing yang kuat. Faktor lain yang mempengaruhi yaitu keterbatasan teknologi pada saat sistem tersebut dibuat, sehingga tidak dirancang untuk menghadapi kemampuan komputasi yang semakin kuat saat ini.

2. Perbedaan antara kelemahan algoritma dengan kelemahan implementasi yaitu kelemahan algoritma terjadi ketika algoritma kriptografi itu sendiri sudah tidak aman, misalnya karena memiliki celah matematis atau sudah berhasil dipecahkan. Sedangkan kelemahan implementasi terjadi bukan karena algoritmanya, tetapi karena kesalahhan dalam penerapannya, seperti penggunaan kunci yang lemah, penyimpanan password yang tidak aman atau konfigurasi sistem yang salah.

3. Organisasi dapat memastikan keamanan sistem kroptografi dengan cara selalu memperbarui algoritma dan standar keamanan yang digunakan sesuai perkembangan teknologi. Selain itu, perlu dilakukan pengujian keamanan secara berkala, seperti penetration testing dan audit sistem. Organisasi juga harus menerapkan praktik keamanan yang baik, seperti manajemen kunci yang benar dan edukasi keamanan bagi pengelola sistem.
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
