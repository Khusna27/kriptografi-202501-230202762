# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: Cipher Modern (DES, AES, RSA) 
Nama: Khusnatun Lina Fitri
NIM: 230202762
Kelas: 5IKRB

---

## 1. Tujuan
1. Mengimplementasikan algoritma **DES** untuk blok data sederhana.  
2. Menerapkan algoritma **AES** dengan panjang kunci 128 bit.  
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma **RSA**.  

---

## 2. Dasar Teori
1. DES (Data Encryption Standard), merupakan algoritma enkripsi simetris dengan panjang kunci 56-bit dan ukuran blok 64-bit serta melibatkan 16 putaran enkripsi yang menggunakan permutasi dan substitusi.
2. AES (Advanced Encryption Standard), digunakan untuk menggantikan DES sebagai standar enkripsi blok dengan ukuran blok 128-bit dan panjang kunci yang dapat berupa 128-bit, 192-bit, atau 256-bit. Memiliki putaran yang berbeda berdasarkan panjang kunci (10, 12, atau 14 putaran). Langkah-langkah utama meliputi AddRoundKey, SubBytes, ShiftRows, MixColumns.
3. RSA (Rivest hamir Adleman), merupakan algoritma asimetris dengan kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Sering digunakan untuk tanda tangan digital.
---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Chrome
- pip install pycryptodome
---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
1. Langkah 1-DES
```
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
```
Hasilnya :
```
Ciphertext: b'\xfb=\x85\x07\x1ba\xb9\xee'
Decrypted: b'ABCDEFGH'
```

2. Langkah 2-AES 128 bit
```
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
Hasilnya :
```
Ciphertext: b'\xe0\x0b\xdf\x84\xdb\x8c\xa5y\xd0U\x18]\x16\xe4\xd6 \x81\x8d\xc5\xc7\xb0\xc83\xb2\xa8'
Decrypted: Modern Cipher AES Example
```
---
3. Langkah 3-RSA
```
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
Hasilnya :
```
Ciphertext: b'Q\xca\xad\xbaQ\xffU\x91w\xaa\xc8 \x86\x08!\xec\x9f~\xc6AM\x90t\xe1\x0fR\x84\x96{0^\x00E>\xf1\xadV7\xdb\xb2\xd4Ys\x141|T8\x1fA\x81\xe2&Je\xc85\\\x0f\t>LS\xce5\x87\xf9e\xcaf\xe2\x02\xe9\x80\x0co&\xa8\xc0\xf6\xf5\xf8\x13\xc9\x9c\t]\xe8\x85\x95(=v2\x9d@\xb3qn\xc4\xe5\xaa\xf5\xb4\xe4r\xbe\x15\xeaK-\x82\x04\x9a\x9c\xf2_\xde"B\x06\xcb\xb0\x15\x93\x00\x19\xc8\x1f\x80\x8e\xd9hU[[\x86q\x88=iJF]\xc5\x98\xcd\xe5\xdd\xb2\x99jY\t\x84\xf7\x8a"\x90\x8fc\xa5/\x04\xfe\x98\xd2\r\x95\x86z\xec\x82\xcc\x1e\xd7u\xa0\xfe\x13\xabz\xe8\x8e-\xff\xed\x04\xe1\x83q\xfc\xd8\xd1Y\xa0\xb8k\xab/\xcb\x1e\xd9\xfd\xaf\xc5ypc\xd6\xf2\x03\x88\\E]\x0c\x83\\\x8e\x1f\xc7\xe8\x16wG\x8b\xd08U\x12\x99\x8b\xa4\xaa~6\xc8\x12[M>{\xe4\xaai\x04\x92F\x9b\'\x81\x9c\xe9<\x05'
Decrypted: RSA Example
```
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
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
