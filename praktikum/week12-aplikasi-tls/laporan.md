# Laporan Praktikum Kriptografi
Minggu ke-: 12

Topik:Aplikasi TLS & E-commerce

Nama: Khusnatun Lina Fitri

NIM: 230202762

Kelas: 5IKRB

---

## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada **email** dan **SSL/TLS**.  
2. Menjelaskan enkripsi dalam transaksi **e-commerce**.  
3. Mengevaluasi isu **etika & privasi** dalam penggunaan kriptografi di kehidupan sehari-hari.  


---

## 2. Dasar Teori

Transport Layer Security (TLS) adalah protokol keamanan yang digunakan untuk melindungi data yang dikirimkan melalui jaringan internet. Protokol ini berfungsi untuk menjaga kerahasiaan dan keutuhan data dengan cara melakukan proses enkripsi antara pengguna dan server. Melalui mekanisme handshake dan penggunaan sertifikat digital, TLS memastikan bahwa komunikasi yang terjadi berlangsung secara aman sehingga data sensitif tidak mudah diakses oleh pihak yang tidak berwenang.

E-commerce merupakan kegiatan transaksi jual beli barang atau jasa yang dilakukan secara elektronik dengan memanfaatkan jaringan internet. Dalam sistem e-commerce, keamanan data menjadi hal yang sangat penting karena proses transaksi melibatkan informasi pribadi dan data pembayaran pengguna. Oleh karena itu, penerapan TLS pada aplikasi e-commerce diperlukan untuk melindungi data dari berbagai ancaman, seperti penyadapan data dan manipulasi informasi selama proses transaksi berlangsung.

Penggunaan TLS pada aplikasi e-commerce dapat meningkatkan tingkat keamanan serta kepercayaan pengguna terhadap layanan yang disediakan. Dengan adanya sistem keamanan yang baik, pengguna akan merasa lebih aman dalam melakukan transaksi secara online. Hal ini memberikan dampak positif bagi pengembangan dan keberlanjutan bisnis e-commerce karena keamanan informasi menjadi salah satu faktor utama dalam keberhasilan sistem perdagangan elektronik.

---

## 3. Alat dan Bahan

- Python 3.x  
- Visual Studio Code 
- Git dan akun GitHub  
- Chrome
---

## 4. Langkah Percobaan

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

1. Apa perbedaan utama antara HTTP dan HTTPS?
2. Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
3.  Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?

Jawaban : 

1. Perbedaan utama antara HTTP dan HTTPS terletak pada aspek keamanannya. HTTP (Hypertext Transfer Protocol) mengirimkan data dalam bentuk teks biasa sehingga mudah disadap atau dimodifikasi oleh pihak yang tidak berwenang. Sementara itu, HTTPS (Hypertext Transfer Protocol Secure) merupakan pengembangan dari HTTP yang menggunakan protokol TLS untuk mengenkripsi data yang dikirimkan antara klien dan server. Dengan adanya enkripsi, HTTPS mampu melindungi informasi sensitif seperti data login dan transaksi online agar tetap aman.

2. Sertifikat digital berperan penting dalam komunikasi TLS karena digunakan untuk memverifikasi identitas server yang diakses oleh pengguna. Sertifikat ini diterbitkan oleh lembaga terpercaya yang disebut Certificate Authority (CA). Dengan adanya sertifikat digital, pengguna dapat memastikan bahwa mereka benar-benar terhubung ke server yang sah dan bukan ke server palsu. Selain itu, sertifikat digital juga digunakan dalam proses pertukaran kunci enkripsi sehingga komunikasi dapat berlangsung secara aman.

3. Kriptografi mendukung privasi dalam komunikasi digital dengan cara mengenkripsi data sehingga hanya pihak yang berwenang yang dapat membaca isi informasi tersebut. Hal ini sangat penting untuk melindungi data pribadi dan mencegah penyalahgunaan informasi. Namun, di sisi lain, penggunaan kriptografi juga menimbulkan tantangan hukum dan etika karena dapat dimanfaatkan untuk menyembunyikan aktivitas ilegal. Kondisi ini menimbulkan dilema antara perlindungan privasi individu dan kepentingan penegakan hukum, sehingga diperlukan regulasi yang seimbang agar kriptografi dapat digunakan secara bertanggung jawab.

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
