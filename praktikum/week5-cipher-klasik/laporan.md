# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik:  Cipher Klasik (Caesar, Vigenère, Transposisi) 
Nama:Khusnatun Lina Fitri 
NIM: 230202762 
Kelas: 5IKRB 

---

## 1. Tujuan
1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori

### 1. Caesar Cipher adalah algoritma enkripsi substitusi paling sederhana yang ditemukan oleh Julius Caesar. Metode ini mengenkripsi teks dengan menggeser setiap huruf sejauh nilai kunci tertentu.  
Contohnya, jika kunci = 3, maka huruf A → D, B → E, dan seterusnya.
Rumus :
C = (P + K) mod 26
P = (C - K) mod 26
Keterangan: 
- `P` = plaintext (huruf asli)  
- `C` = ciphertext (huruf hasil enkripsi)  
- `K` = kunci pergeseran  
Metode ini mudah dipahami dan diimplementasikan, tetapi keamanannya rendah karena pola huruf masih bisa ditebak melalui analisis frekuensi.

---
### 2. Vigenère Cipher
Vigenère Cipher merupakan pengembangan dari Caesar Cipher yang menggunakan kata kunci (key) untuk menentukan jumlah pergeseran pada tiap huruf. Setiap huruf digeser berdasarkan nilai karakter dalam kunci, sehingga pola pergeseran berubah-ubah dan lebih sulit ditebak.
Rumus:

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
### Langkah 1 - Implementasi Caesar Cipher
```
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasilnya : 
```
Plaintext : CLASSIC CIPHER
Ciphertext: FODVVLF FLSKHU
Decrypted : CLASSIC CIPHER
```

### Langkah 2 - Implementasi Vigenere Cipher

```
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasilnya : 
```
Plaintext : KRIPTOGRAFI
Ciphertext: UVGZXMQVYPM
Decrypted : KRIPTOGRAFI
```

### Langkah 3 - Implementasi Transposisi Sederhana
```
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasilnya :
```
Plaintext : TRANSPOSITIONCIPHER
Ciphertext: TPIPROOHASNENICRSTI
Decrypted : TRANSPOSITIONCIPHER
```

### Langkah 4 - Contoh uji coba ketiganya
```

#  CAESAR CIPHER


def caesar_encrypt(plaintext, key):
    """Mengenkripsi teks menggunakan Caesar Cipher"""
    result = ""
    for char in plaintext:
        if char.isalpha():  # hanya huruf yang dienkripsi
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # karakter non-huruf tidak berubah
    return result


def caesar_decrypt(ciphertext, key):
    """Mendekripsi teks Caesar Cipher"""
    return caesar_encrypt(ciphertext, -key)


# --- Contoh Uji Caesar Cipher ---
msg = "ILMU KOMPUTER "
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)

print("=== CAESAR CIPHER ===")
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
print()


#  VIGENÈRE CIPHER


def vigenere_encrypt(plaintext, key):
    """Mengenkripsi teks menggunakan Vigenère Cipher"""
    result = []
    key = key.lower()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


def vigenere_decrypt(ciphertext, key):
    """Mendekripsi teks Vigenère Cipher"""
    result = []
    key = key.lower()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


# --- Contoh Uji Vigenère Cipher ---
msg = "ILMU KOMPUTER"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)

print("=== VIGENÈRE CIPHER ===")
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
print()



# TRANSPOSITION CIPHER


def transpose_encrypt(plaintext, key=5):
    """Mengenkripsi teks menggunakan Transposition Cipher"""
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)


def transpose_decrypt(ciphertext, key=5):
    """Mendekripsi teks Transposition Cipher"""
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        # Jika kolom penuh, lanjut ke baris berikutnya
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# --- Contoh Uji Transposition Cipher ---
msg = "ILMU KOMPUTER"
key = 5
enc = transpose_encrypt(msg, key)
dec = transpose_decrypt(enc, key)

print("=== TRANSPOSITION CIPHER ===")
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)


```
Hasilnya :
```
=== CAESAR CIPHER ===
Plaintext : ILMU KOMPUTER   
Ciphertext: LOPX NRPSXWHU   
Decrypted : ILMU KOMPUTER   

=== VIGENÈRE CIPHER ===     
Plaintext : ILMU KOMPUTER   
Ciphertext: SPKE OMWTSDIP   
Decrypted : ILMU KOMPUTER   

=== TRANSPOSITION CIPHER ===
Plaintext : ILMU KOMPUTER   
Ciphertext: IKTLOEMMRUP U   
Decrypted : ILMU KOMPUTER
```
---

## 6. Hasil dan Pembahasan

### 1. Caesar Cipher

![Hasil Eksekusi](screenshots/langkah-1-caesar-cipher.png)

Pembahasan : Penerapan caesar cipher pada source code dengan pergeseran huruf sejauh 3 huruf (key = 3) dengan plaintext "CLASSIC CIPHER" kemudian di enkripsi dengan pergeseran 3 huruf menjadi "FODVVLF FLSKHU" dan pada saat dekripsi berhasil menghasilkan teks yang telah dienkripsi yaitu "CLASSIC CIPHER". Namun penggunaan caesar cipher sangat mudah dipecahkan karena hanya memiliki 25 kemungkinan kunci dan rentan terhadap serangan brute force.

### 2. Vigenere Cipher

![Hasil Eksekusi](screenshots/langkah-2-vignere%20-cipher.png)

Pembahasan : Berdasarkan source code nya penerapan vigenere cipher menggunakan kata kunci "key" untuk pergeseran setiap hurufnya. Jadi huruf pertama digeser berdasar huruf pertama dari "KEY", huruf kedua menggunakan huruf kedua dari "KEY", dan seterusnya. Sehingga penerapannya menjadi plaintext="KRIPTOGRAFI" dengan kunci="KEY" kemudian dienkripsi menjadi "UVGZXMQVYPM" dan dilakukan dekripsi menjadi "KRIPTOGRAFI". Keamanan vigenere cipher lebih baik dibandingkan caesar cipher karena setiap huruf digeser dengan pola berbeda sesuai kunci, namun jika kunci terlalu pendek akan mudah dipecahkan dengan pola analisis seperti penggunaan metode kasiski examination. Jadi sebaiknya penggunaan kunci pada vigenere cipher dibuat lebih panjang dan acak untuk keamanan yang lebih baik. 

### 3. Transpos Cipher

![Hasil Eksekusi](screenshots/langkah3-transposisi-sederhana.png)

Pembahasan :Penerapan transpose cipher tidak mengubah hurufnya melainkan mengubah urutan posisi huruf. Seperti penerapan pada source code dengan palintext "TRANSPOSITIONCIPHER" kemudian dienkripsi dengan key="5" menjadi "TPIRPOHOASNENICRSTI" dan pada saat dilakukan dekripsi kembali menjadi teks asli yaitu "TRANSPOSITIONCIPHER". Jika dibandingkan dengan caesar cipher dan vigenere cipher keamanan pada transpose cipher lebih baik karena enkripsi akan sulit dibaca tanpa mengetahui kuncinya, namun jika panjang pesan dan panjang kunci diketahui akan mudah untuk dianalisis. Jadi sebaiknya transpose cipher tidak digunakan sendiri melainkan dikombinasikan dengan cipher lain seperti caesar maupun vigenere cipher supaya keamanannya jauh lebih kuat.

### 4. Hasil eksekusi program uji coba

![Hasil Eksekusi](screenshots/hasil.png)

Pembahasan : Secara keseluruhan, hasil percobaan menunjukan keberhasilan dalam penerapannya. Seperti pada gambar diatas dengan mengubah plaintext menjadi "ILMU KOMPUTER" kemudian diterapkan pada ketiga algoritma semuanya berjalan dengan baik atau dengan kata lain plaintext dapat dienkripsi dan kemudian di dekripsi kembali ke bentuk yang asli dengan kunci yang sesuai.

---

## 7. Jawaban Pertanyaan

1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?  
2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?  
3. Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.  

Jawaban :
1. Kelemahan caesar cipher adalah terlalu sederhana dan mudah ditebak karena hanya menggunakan satu nilai geser dengan 25 kemungkinan percobaan. Selain itu karena hanya ada ada 25 kemungkinan percobaan maka pola huruf mudah ditebak dengan analisis frekuensi dan sangat rentan terhadap serangan brute force. Sedangkan kelemahan  Vigenère cipher terletak pada panjangnya kunci, meskipun lebih kuat dari pada caesar cipher karena bersifat polialfabetik jika kunci terlalu pendek pola nya akan lebih mudah untuk ditebak dan diserang menggunakan metode seperti kasiski examination.

2. Cipher klasik mudah diserang dengan analisis frekuensi karena tidak mengubah pola kemunculan huruf dalam teks. Contohnya dalam setiap bahasa, terdapat pola frekuensi huruf yang khas seperti penggunaan bahasa Indonesia frekuensi huruf "A" lebih sering muncul sehingga pola kemunculannya mudah ditebak dengan pola distribusi. Selain itu penyerang juga dapat membandingkan frekuensi kemunculan huruf pada ciphertext dengan pola frekuensi umum suatu bahasa untuk menebak huruf-huruf yang disubstitusi.

3. Chiper substitusi bekerja dengan mengganti setiap huruf pada text menjadi huruf lain berdasarkan aturan kunci tertentu. Sedangkan transposisi tidak mengganti huruf, melainkan mengubah urutan huruf dalam teks sehingga pesan sulit dibaca tanpa kunci yang benar. Kelebihan cipher substitusi yaitu proses enkripsi sederhana dan cepat sehingga cocok untuk menjelaskan konsep dasar kriptografi sedangkan kelemahannya yaitu pola huruf mudah ditebak dengan analisis frekuensi dan keamananya rendah jika tidak di kombinasikan dengan algoritma lain. Sedangkan kelebihan transposisi adalah huruf asli tidak diganti melainkan hanya posisinya saja yang diacak sehingga pola huruf lebih sulit untuk dikenali dan lebih kuat jika dikombinasikan dengan cipher substitusi dan kelemahannya jika kunci atau pola pengacakan diketahui maka pesan mudah dipecahkan dan kurang efektif jika digunakan sendiri tanpa variasi pola.
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
