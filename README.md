# CAPFIZZ BOT
Bot otomatis yang mengakses API `mainnet.capfizz.com` menggunakan proxy untuk berbagai fungsi seperti autentikasi, monitoring uptime, dan mining.

REGISTER
## https://mainnet.capfizz.com/register?ref=XE3P0O

## Ambil cookie seperti di gambar
![banner](./cookie.png)
## 📌 Fitur
- 🔹 **Autentikasi Otomatis**: Login dengan sesi yang disimpan di `cookie.txt`
- 🔹 **Pemilihan Proxy**: Gunakan daftar proxy dari `proxy.txt`
- 🔹 **Monitoring Uptime**: Mengecek status uptime secara berkala
- 🔹 **Mining Node**: Mengirim request mining otomatis
- 🔹 **Cek Poin User**: Mengecek poin akun yang terhubung
- 🔹 **Looping & Sinkronisasi**: Berjalan terus-menerus dengan interval 1 menit

---

## 📥 Instalasi

### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/adhe222/capfizz-bot.git
cd capfizz-bot
```

### 2️⃣ **Instal Dependensi**
Pastikan Python sudah terinstal. Kemudian jalankan:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Konfigurasi**
- **Cookie Autentikasi**: Simpan cookie sesi di `cookie.txt`
- **Proxy**: Tambahkan daftar proxy di `proxy.txt`

### 4️⃣ **Menjalankan Bot**
```bash
python bot.py
```

---
![banner](./img2.png)

## ⚙️ Konfigurasi Tambahan
- **Mengubah interval waktu**: Edit `time.sleep(60)` di script utama untuk menyesuaikan delay.
- **Logging**: Tambahkan logging jika ingin menyimpan aktivitas bot.

---

