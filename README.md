# 🔐 Ransim - Simulasi Ransomware Edukasi

**Ransim** adalah sebuah aplikasi simulasi ransomware yang dibuat menggunakan Python. Proyek ini bertujuan untuk pembelajaran dan edukasi, terutama bagi mereka yang ingin memahami bagaimana proses enkripsi dan dekripsi file dalam skenario ransomware — namun tanpa efek berbahaya.

---

## 🧩 Fitur Utama

- Enkripsi file dalam folder tertentu dengan password.
- Dekripsi file hanya jika password yang benar dimasukkan.
- Tampilan simulasi ransomware dengan timer hitung mundur.
- Antarmuka pengguna (GUI) berbasis Tkinter.
- Menggunakan pustaka `cryptography` untuk keamanan data.

---

## ⚙️ Cara Menggunakan

1. Jalankan program `ransom.py`.
2. Pilih folder yang ingin dienkripsi.
3. Masukkan password enkripsi.
4. Jendela simulasi ransomware muncul.
5. Masukkan password untuk dekripsi. Jika benar, file akan dikembalikan.

---

## 📥 Instalasi

Pastikan Python (disarankan versi 3.8+) sudah terpasang di sistem kamu.

Instal dependensi:

```bash
git clone https://github.com/Wh1teLine/ransim.git
cd ransim
python ransim.py
