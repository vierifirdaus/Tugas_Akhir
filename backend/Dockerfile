# backend/Dockerfile

# Gunakan base image yang lebih spesifik untuk python 3.11
FROM python:3.11-slim

# Atur direktori kerja di dalam container
WORKDIR /app

# Install dependensi sistem (Graphviz) dan bersihkan cache dalam satu layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends graphviz && \
    rm -rf /var/lib/apt/lists/*

# Salin file requirements terlebih dahulu untuk memanfaatkan caching Docker
# Ini mencegah pip install berjalan ulang setiap kali kode berubah
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin sisa kode aplikasi ke dalam direktori kerja
COPY . .

# Buat direktori public (jika masih diperlukan)
RUN mkdir -p ./public

# Hapus variabel FLASK_ENV, karena Gunicorn akan berjalan dalam mode produksi secara default
# ENV FLASK_ENV=development <-- Dihapus

# EXPOSE tidak wajib karena port diatur di docker-compose, tapi ini adalah dokumentasi yang baik
EXPOSE 5001

# Jalankan aplikasi menggunakan Gunicorn
# --bind 0.0.0.0:5001 -> Jalankan di semua network interface pada port 5001
# --workers 3 -> Contoh: Gunakan 3 worker process (sesuaikan dengan kebutuhan)
# run:app -> Cari instance 'app' di dalam file 'run.py'
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers=3", "run:app"]