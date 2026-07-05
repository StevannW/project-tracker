# 📝 Project Tracker Website


## 🐋 Opsi 1: Setup Menggunakan Docker
## Persiapan
Jika ingin melakukan setup menggunakan docker, install terlebih dahulu aplikasi docker desktop:
- https://www.docker.com/products/docker-desktop/

Jika sudah memiliki aplikasi docker, berikut langkah langkahnya:

### 1. Clone Repository
Unduh kode sumber proyek ini ke device.

Buka terminal di device, lalu ketik command:
```bash
git clone https://github.com/StevannW/project-tracker.git
```
```bash
cd project-tracker
```

### 2. Atur Environment dan Jalankan Docker
Salin file kredensial contoh yaitu `.env.example` menjadi file `.env` resmi. Jalankan perintah ini di terminal:

```bash
# Untuk pengguna macOS / Linux:
cp backend/.env.example backend/.env

# Untuk pengguna Windows (Command Prompt):
copy backend\.env.example backend\.env
```

Setelah file `.env` berhasil diduplikasi, jalankan perintah `docker compose`:
```bash
docker compose up --build
```
> *Proses ini akan mengunduh Image PostgreSQL, mem-build Backend, mem-build Frontend secara statis, dan menjalankan ketiganya secara otomatis dan terisolasi.*

### 3. Akses Aplikasi
Setelah log di terminal menunjukkan bahwa semua *container* sudah berjalan (Started/Running), buka browser dan kunjungi:

- 🌐 **Aplikasi Utama (Frontend)**: [http://localhost](http://localhost)
- 📖 **Dokumentasi API (Backend/Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)

### Menghentikan Aplikasi
Tekan `Ctrl+C` pada terminal yang sedang berjalan. Jika ingin mematikan *container* yang berjalan di latar belakang secara bersih, gunakan:
```bash
docker compose down
```
*(Opsional)* Jika Anda ingin mereset/menghapus seluruh isi database task yang tersimpan:
```bash
docker compose down -v
```

---



## 💻 Opsi 2: Setup Manual (Tanpa Docker)

## Persiapan
Jika ingin menjalankan aplikasi secara manual tanpa Docker, pastikan aplikasi berikut sudah terinstal di komputer:
- [PostgreSQL 16+](https://www.postgresql.org/download/)
- [Python 3.13+](https://www.python.org/downloads/)
- [Node.js 22+](https://nodejs.org/)

Untuk memastikan aplikasi tersebut sudah terinstal dengan benar beserta versinya, Anda bisa menjalankan perintah berikut di terminal:
```bash
psql -V
python --version
node -v
```

Jika sudah memiliki aplikasi aplikasi diatas, berikut langkah langkahnya:

### 1. Clone Repository
```bash
git clone https://github.com/StevannW/project-tracker.git
```

```bash
cd project-tracker
```

### 2. Setup Database PostgreSQL
Pastikan layanan database PostgreSQL sudah berjalan di perangkat Anda. Buka pgAdmin (atau CLI `psql`), lalu buat sebuah database baru dengan nama `task_tracker`:
```sql
CREATE DATABASE task_tracker;
```

### 3. Setup Backend (Python / FastAPI)
Buka terminal dan masuk ke folder `backend`:
```bash
cd backend
```
Buat lingkungan virtual (*Virtual Environment*) agar instalasi library terisolasi:
```bash
python -m venv .venv

# Aktivasi di Windows:
.venv\Scripts\activate

# Aktivasi di macOS / Linux:
source .venv/bin/activate
```
Instal library yang diperlukan:
```bash
pip install -r requirements.txt
```
Salin file konfigurasi:
```bash
# Windows:
copy .env.example .env
# macOS/Linux:
cp .env.example .env
```
> ⚠️ **SANGAT PENTING**: Buka file `backend/.env` yang baru dibuat. Anda **wajib** mengubah nilai `DATABASE_USER` dan `DATABASE_PASSWORD` dengan kredensial PostgreSQL asli komputer Anda.

Jalankan Server Backend:
```bash
uvicorn app.main:app --reload
```
API sekarang berjalan di **http://localhost:8000**. Skema database/tabel akan secara otomatis dibuat saat server pertama kali menyala!

### 4. Setup Frontend (Node / Vue)
Buka tab terminal baru (biarkan terminal backend tetap berjalan) dan masuk ke folder `frontend`:
```bash
cd frontend
```
Instal semua paket dependensi Node.js:
```bash
npm install
```
Salin file konfigurasi:
```bash
# Windows:
copy .env.example .env
# macOS/Linux:
cp .env.example .env
```
> *(File frontend/.env secara default sudah mengarah ke backend lokal Anda).*

Jalankan Development Server Vite:
```bash
npm run dev
```
Aplikasi antarmuka/frontend Anda sekarang berjalan secara *live* di **http://localhost:5173**.