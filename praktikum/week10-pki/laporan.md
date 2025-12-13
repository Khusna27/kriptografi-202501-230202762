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

Public Key Infrastructure (PKI) merupakan sebuah kerangka kerja kriptografi yang penting dalam keamanan digital karena memungkinkan pengelolaan sertifikat digital dan pasangan kunci publik–privat untuk keperluan autentikasi, enkripsi, dan integritas data dalam komunikasi jaringan. Dalam PKI, sertifikat digital mengikuti standar seperti X.509 yang mengikat identitas suatu entitas dengan kunci publiknya melalui tanda tangan digital dan diverifikasi oleh pihak tepercaya agar dapat dipercaya oleh pengguna lain dalam sistem komunikasi. Standar X.509 sendiri menjadi dasar dalam berbagai protokol aman termasuk TLS/SSL yang digunakan dalam HTTPS. 

Peran Certificate Authority (CA) dalam sistem PKI sangat sentral karena CA bertanggung jawab untuk memverifikasi identitas pemohon sertifikat sebelum menerbitkan sertifikat digital yang valid. Dalam hierarki PKI yang umum, root CA berada pada tingkat tertinggi sebagai sumber kepercayaan utama, dan dapat mendelegasikan tugas penerbitan ke intermediate CA untuk meningkatkan keamanan operasional dan skalabilitas sistem. Hal ini membantu memastikan bahwa sertifikat yang diterbitkan benar-benar berasal dari sumber tepercaya.

Fungsi sistem PKI juga terlihat jelas dalam konteks komunikasi aman seperti HTTPS dan protokol TLS, di mana sertifikat digital yang diterbitkan oleh CA memungkinkan browser dan server untuk melakukan handshake yang terenkripsi dan saling memverifikasi identitas masing-masing pihak. Dengan demikian, data yang ditransmisikan terlindungi dari penyadapan atau modifikasi oleh pihak yang tidak berwenang, sehingga menjaga kerahasiaan dan keutuhan informasi. 

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Schollar 

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

1. Apa fungsi utama Certificate Authority (CA)?  
2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?  
3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?  

Jawaban : 

1. Fungsi utama Certificate Authority (CA) adalah sebagai lembaga tepercaya yang berperan dalam menjamin keaslian identitas suatu entitas di dalam sistem keamanan berbasis PKI. CA bertugas melakukan proses verifikasi identitas sebelum menerbitkan sertifikat digital, sehingga kunci publik yang tercantum di dalam sertifikat benar-benar dimiliki oleh pihak yang bersangkutan. Selain menerbitkan sertifikat, CA juga mengelola masa berlaku sertifikat, melakukan pembaruan, serta menyediakan mekanisme pencabutan sertifikat apabila terjadi penyalahgunaan atau kebocoran kunci. Dengan adanya CA, kepercayaan antar pihak dalam komunikasi digital dapat terbangun tanpa harus saling mengenal secara langsung.

2. Self-signed certificate tidak cukup digunakan pada sistem produksi karena sertifikat jenis ini diterbitkan dan ditandatangani oleh pemiliknya sendiri tanpa melibatkan pihak ketiga yang tepercaya. Akibatnya, klien atau browser tidak memiliki dasar untuk memastikan bahwa identitas server tersebut benar dan bukan tiruan. Hal ini biasanya ditandai dengan munculnya peringatan keamanan pada browser, yang dapat menurunkan kepercayaan pengguna terhadap sistem. Selain itu, penggunaan self-signed certificate meningkatkan risiko serangan seperti penyamaran identitas (spoofing), sehingga sertifikat ini lebih cocok digunakan pada tahap pengembangan, pengujian, atau pembelajaran, bukan pada lingkungan produksi yang melibatkan pengguna umum.

3. PKI mencegah serangan Man-in-the-Middle (MITM) dalam komunikasi TLS/HTTPS melalui mekanisme verifikasi sertifikat dan enkripsi komunikasi. Ketika klien mengakses sebuah server HTTPS, klien akan memeriksa sertifikat digital server tersebut, termasuk keabsahan tanda tangan CA, kesesuaian nama domain, dan masa berlaku sertifikat. Jika sertifikat dinyatakan valid, proses handshake TLS akan dilanjutkan untuk membentuk kunci sesi yang digunakan dalam enkripsi data. Dengan cara ini, pihak ketiga yang mencoba menyadap atau memodifikasi komunikasi tidak dapat membaca isi data karena terenkripsi, serta tidak dapat menyamar sebagai server yang sah karena tidak memiliki sertifikat valid yang diterbitkan oleh CA tepercaya.

---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka

- Wathoni, M., Nurhasanah, R., Shela, D., Informasi, P. T., Pendidikan, F. I., Muhammadiyah, U., & Selatan, K. T. (n.d.). Penerapan konfigurasi dasar pki dua tingkat: active directory certificate services (ad cs). 55–62.

---

## 10. Commit Log

```
commit week10-pki
Author: Khusnatun Lina Fitri <husnatunlinafitri@gmail.com>
Date:   2025-12-13

   week10-pki : Public Key Infrastructure (PKI & Certificate Authority)

```
