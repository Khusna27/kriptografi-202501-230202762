# Laporan Praktikum Kriptografi
Minggu ke-: 15
Topik: Proyek Kelompok – TinyCoin ERC20
Nama:Khusnatun Lina Fitri
NIM: 230202762
Kelas: 5IKRB

---

## 1. Tujuan

1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3. Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori

TinyCoin merupakan token digital yang dibangun di atas blockchain Ethereum dengan menggunakan standar ERC-20. Ethereum menyediakan platform terdesentralisasikan yang mendukung eksekusi smart contract, yaitu program yang berjalan otomatis di jaringan blockchain. Dengan smart contract, seluruh transaksi TinyChoin dicatat secara transparan, aman, dan tidak dapat diubah, sehingga tidak memerlukan pihak ketiga sebagai perantara.

Standar ERC-20 mendefinisikan fungsi dasar seperti transfer, balance0f, dan totalSupply agar token dapat digunakan secara luas pada ekosistem Ethereum termasuk wallet dan aplikasi terdesentralisasi. Dengan mengikuti standar ini, TinyChoin menjadi kompatibel dengan berbagai layanan blockchain tanpa perlu penyesuaian tambahan.

TinyCoin digunakan sebagai token pembelajaran untuk memahami konsep dasar kriptografi dan blockchain, khususnya pengelolaan aset digital berbasis smart contract. Melalui implementasi TinyCoin ERC-20, pengguna dapat mempelajari proses pembuatan token, pengiriman aset digital, serta pentingnya keamanan smart contract dalam menjaga keandalan sistem blockchain.

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

### Langkah 1 - Mmebuat Kontrak ERC-20.

Membuat file dengan nama TinyCoin.sol diremix ide.
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TinyCoin {

    // =========================
    // Informasi Token
    // =========================
    string public name = "TinyCoin";
    string public symbol = "TNC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // =========================
    // Penyimpanan Saldo
    // =========================
    mapping(address => uint256) public balanceOf;

    // =========================
    // Event (standar ERC20)
    // =========================
    event Transfer(address indexed from, address indexed to, uint256 value);

    // =========================
    // Constructor
    // =========================
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * 10 ** uint256(decimals);
        balanceOf[msg.sender] = totalSupply;
    }

    // =========================
    // Fungsi Transfer
    // =========================
    function transfer(address to, uint256 amount) public returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Saldo tidak cukup");
        require(to != address(0), "Alamat tidak valid");

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }
}
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

1. Apa fungsi utama ERC20 dalam ekosistem blockchain?  
2. Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20?  
3. Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya?

Jawaban :

1. ERC20 berfungsi sebagai standar pembuatan token di blockchain Ethereum. Dengan adanya standar ini, token yang dibuat bisa digunakan dan dikenali oleh berbagai wallet, exchange, dan aplikasi berbasis blockchain tanpa perlu penyesuaian tambahan. ERC20 memudahkan pengembang dalam membuat token dan memastikan token tersebut kompatibel dengan ekosistem Ethereum.

2.Transfer token pada ERC20 dilakukan menggunakan fungsi transfer. Ketika fungsi ini dijalankan, sistem akan mengecek saldo pengirim terlebih dahulu. Jika saldo mencukupi, maka saldo pengirim akan dikurangi dan saldo penerima akan ditambahkan sesuai jumlah token yang dikirim. Semua transaksi ini dicatat di blockchain sehingga transparan dan tidak bisa diubah.

3. Risiko utama dalam smart contract biasanya berasal dari kesalahan penulisan kode atau logika program yang kurang tepat, sehingga bisa dimanfaatkan oleh pihak lain. Untuk mengurangi risiko tersebut, pengembang dapat menggunakan library yang sudah terpercaya seperti OpenZeppelin, memakai versi Solidity terbaru, serta melakukan pengujian dan audit sebelum smart contract dijalankan di jaringan utama.
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
