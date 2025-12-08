# Laporan Praktikum Kriptografi
Minggu ke-: 9
Topik: Digital Signature (RSA/DSA) 
Nama:Khusnatun Lina Fitri
NIM: 230202762
Kelas: 5IKRB

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.  
2. Memverifikasi keaslian tanda tangan digital.  
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.  
---

## 2. Dasar Teori
  Tanda tangan digital dengan RSA pada dasarnya memanfaatkan konsep kriptografi kunci publik. Prosesnya dimulai dengan membuat hash dari pesan, kemudian hash tersebut ditandatangani menggunakan private key pengirim. Saat penerima mendapatkan pesan, ia cukup memverifikasi tanda tangan tersebut dengan public key pengirim dan mencocokkannya dengan hash asli. Kelebihan RSA adalah mekanismenya cukup sederhana dan sudah banyak digunakan dalam berbagai sistem keamanan.

Sementara itu, DSA (Digital Signature Algorithm) menggunakan pendekatan matematika yang berbeda, yaitu operasi logaritma diskret pada bidang bilangan modular. Algoritma ini dikenal lebih cepat dalam proses pembuatan tanda tangan, walaupun tahap verifikasinya bisa sedikit lebih lambat dibanding RSA. DSA juga sangat bergantung pada nilai acak (nonce) yang harus berbeda setiap kali menandatangani, karena jika nilai ini terulang, keamanan sistem bisa langsung terganggu.

Secara keseluruhan, baik RSA maupun DSA sama-sama dipakai untuk memastikan keaslian, integritas, serta mencegah penyangkalan terhadap suatu pesan digital. Perbedaannya terletak pada metode matematis dan performanya, tetapi keduanya tetap menjadi bagian penting dalam teknologi keamanan modern yang sering dipelajari di dunia akademik.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code 
- Git dan akun GitHub  
- Google Chrome

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
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?

Jawaban : 

1. Perbedaan Utama Enkripsi RSA dan Digital Signature RSA ada pada tujuan serta arah penggunaan kunci yang berbeda:

    a. Enkripsi RSA

     - Pengirim mengenkripsi pesan menggunakan public key penerima.
       
     - Penerima membuka pesan dengan private key miliknya.
       
     - Tujuan utama: menjaga kerahasiaan pesan (confidentiality).

    b. Tanda Tangan Digital RSA
   
     - Pengirim menandatangani pesan menggunakan private key miliknya.
     
     - Penerima memverifikasi tanda tangan menggunakan public key pengirim.
       
     - Tujuan utama: menjamin keaslian (authenticity) dan integritas pesan.

2. Karena tanda tangan digital memanfaatkan hashing untuk membuat sidik jari pesan. Ketika pesan diubah sedikit saja, nilai hash akan berubah total sehingga proses verifikasi langsung gagal. Karena tanda tangan hanya dapat dibuat menggunakan private key pemiliknya, siapa pun yang memverifikasi tanda tangan dengan public key pengirim dapat memastikan:

    - Pesan tidak diubah → integrity

    - Pesan benar dari pengirim yang sah → authenticity

3. Peran Certificate Authority (CA) dalam sistem digital signature adalah sebagai pihak ketiga yang berfungsi untuk:

    - Memverifikasi identitas pemilik kunci publik

    - Menerbitkan digital certificate yang menghubungkan identitas seseorang/organisasi dengan public key

    - Menjadi dasar trust dalam sistem keamanan modern seperti HTTPS, email secure, dan dokumen bertanda tangan digital

    Dengan CA, pengguna tidak perlu ragu terhadap keaslian sebuah public key, sehingga sistem tanda tangan digital dapat berjalan dengan aman dan dapat dipercaya.
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka 
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit week9-digital-signature
Author: Khusnatun Lina Fitri <husnatunlinafitri@gmail.com>
Date:   2025-11-08

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
