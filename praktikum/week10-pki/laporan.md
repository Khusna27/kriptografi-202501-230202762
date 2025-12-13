# Laporan Praktikum Kriptografi
Minggu ke-: 10 
Topik: Public Key Infrastructure (PKI & Certificate Authority)  
Nama: Khusnatun Lina Fitri
NIM: 230202762  
Kelas:5IKRB 

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.  
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.  
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).  

---

## 2. Dasar Teori

Public Key Infrastructure (PKI) merupakan sebuah kerangka kerja kriptografi yang penting dalam keamanan digital karena memungkinkan pengelolaan sertifikat digital dan pasangan kunci publik–privat untuk keperluan autentikasi, enkripsi, dan integritas data dalam komunikasi jaringan. Dalam PKI, sertifikat digital mengikuti standar seperti X.509 yang mengikat identitas suatu entitas dengan kunci publiknya melalui tanda tangan digital dan diverifikasi oleh pihak tepercaya agar dapat dipercaya oleh pengguna lain dalam sistem komunikasi. Standar X.509 sendiri menjadi dasar dalam berbagai protokol aman termasuk TLS/SSL yang digunakan dalam HTTPS. Dengan memahami struktur dan prinsip kerja PKI ini, mahasiswa dapat belajar membuat sertifikat digital sederhana sebagai bagian dari proses otentikasi dan enkripsi data. 


Peran Certificate Authority (CA) dalam sistem PKI sangat sentral karena CA bertanggung jawab untuk memverifikasi identitas pemohon sertifikat sebelum menerbitkan sertifikat digital yang valid. Dalam hierarki PKI yang umum, root CA berada pada tingkat tertinggi sebagai sumber kepercayaan utama, dan dapat mendelegasikan tugas penerbitan ke intermediate CA untuk meningkatkan keamanan operasional dan skalabilitas sistem. Struktur seperti ini membantu memastikan bahwa sertifikat yang diterbitkan benar-benar berasal dari sumber tepercaya. Riset tentang hierarki PKI menekankan pentingnya desain dan manajemen CA untuk meningkatkan keamanan jaringan, khususnya dalam mempertahankan kepercayaan terhadap sertifikat digital yang digunakan di berbagai aplikasi. 


Fungsi sistem PKI juga terlihat jelas dalam konteks komunikasi aman seperti HTTPS dan protokol TLS, di mana sertifikat digital yang diterbitkan oleh CA memungkinkan browser dan server untuk melakukan handshake yang terenkripsi dan saling memverifikasi identitas masing-masing pihak. Dengan demikian, data yang ditransmisikan terlindungi dari penyadapan atau modifikasi oleh pihak yang tidak berwenang, sehingga menjaga kerahasiaan dan keutuhan informasi. Studi-studi tentang manajemen sertifikat juga mengangkat isu-isu terkini seperti otomatisasi sertifikat dan validasi jalur sertifikasi (certification path validation algorithm) yang menjadi bagian penting dalam memastikan keandalan sistem PKI di lingkungan global. 


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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
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
commit week10-pki
Author: Khusnatun Lina Fitri <husnatunlinafitri@gmail.com>
Date:   2025-12-13

   week10-pki : Public Key Infrastructure (PKI & Certificate Authority)

```
