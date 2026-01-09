# Laporan Praktikum Kriptografi

Minggu ke-: 13

Topik: TinyChain – Proof of Work (PoW)

Nama: Khusnatun Lina Fitri

NIM: 230202762

Kelas: 5IKRB

---

## 1. Tujuan
1. Menjelaskan peran **hash function** dalam blockchain.  
2. Melakukan simulasi sederhana **Proof of Work (PoW)**.  
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.  
---

## 2. Dasar Teori

Blockchain merupakan teknologi penyimpanan data terdistribusi yang menyimpan catatan transaksi dalam bentuk blok yang saling terhubung dan diamankan menggunakan teknik kriptografi. Setiap blok berisi data transaksi, hash dari blok sebelumnya, serta nilai hash blok itu sendiri, sehingga membentuk rantai yang sulit untuk diubah. Konsep ini memungkinkan terciptanya sistem yang transparan, aman, dan tidak bergantung pada satu pihak pusat. TinyChain merupakan implementasi blockchain sederhana yang digunakan untuk memahami konsep dasar blockchain, termasuk mekanisme konsensus yang digunakan.

Proof of Work (PoW) adalah salah satu mekanisme konsensus yang digunakan dalam blockchain untuk memverifikasi dan menambahkan blok baru ke dalam rantai. Pada PoW, setiap node atau penambang harus menyelesaikan permasalahan komputasi berupa pencarian nilai hash yang memenuhi tingkat kesulitan tertentu. Proses ini membutuhkan daya komputasi yang besar, sehingga menyulitkan pihak yang tidak berwenang untuk memanipulasi data. Dengan adanya PoW, hanya node yang berhasil menyelesaikan perhitungan yang berhak menambahkan blok baru, sehingga keamanan dan keutuhan data blockchain dapat terjaga.

Dalam konteks TinyChain, PoW digunakan sebagai simulasi untuk menunjukkan bagaimana proses penambangan dan validasi blok dilakukan. Meskipun berskala kecil dan tidak sekompleks blockchain publik seperti Bitcoin, TinyChain mampu menggambarkan prinsip kerja PoW secara jelas, mulai dari proses hashing, penentuan tingkat kesulitan, hingga pembentukan blok yang saling terhubung. Dengan demikian, TinyChain menjadi media pembelajaran yang efektif untuk memahami konsep dasar Proof of Work dalam teknologi blockchain.

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

1. Mengapa fungsi hash sangat penting dalam blockchain?  
2. Bagaimana Proof of Work mencegah double spending?  
3. Apa kelemahan dari PoW dalam hal efisiensi energi?  

Jawaban : 
1. Fungsi hash sangat penting dalam teknologi blockchain karena berperan sebagai identifikasi unik untuk setiap blok data dan memastikan integritas serta keamanan seluruh rantai blok; setiap perubahan sekecil apa pun pada isi blok akan menghasilkan nilai hash yang sangat berbeda, sehingga memudahkan deteksi manipulasi data, dan karena setiap blok menyimpan hash dari blok sebelumnya, struktur ini membuat rantai blok sulit diubah tanpa konsensus jaringan.

2. Proof of Work (PoW) mencegah double spending dengan mewajibkan penambang melakukan kerja komputasi besar untuk menambahkan blok baru ke blockchain, sehingga setiap transaksi harus divalidasi dan dimasukkan dalam blok yang telah melalui proses hashing kompleks, dan karena manipulasi blok yang telah diterima membutuhkan perhitungan ulang seluruh rantai yang sangat mahal secara komputasi dan tidak praktis, percobaan menggunakan satu aset digital lebih dari sekali akan ditolak oleh jaringan.

3. Kelemahan utama dari mekanisme konsensus Proof of Work adalah konsumsi energi yang sangat tinggi karena penambang harus terus melakukan perhitungan komputasi kompleks untuk menemukan nilai hash yang memenuhi tingkat kesulitan, sehingga proses mining memerlukan daya listrik dan sumber daya komputasi yang besar yang berdampak pada biaya operasional tinggi dan dampak lingkungan, menjadikan PoW kurang efisien dibandingkan mekanisme lain yang lebih hemat energi seperti Proof of Stake.
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
