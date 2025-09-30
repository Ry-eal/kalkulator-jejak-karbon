# kalkulator-jejak-karbon
Aplikasi Streamlit untuk menghitung jejak karbon dengan feedback AI

# 🌍 Kalkulator Jejak Karbon Pribadi

## 1. Deskripsi Singkat

Aplikasi Python interaktif ini dibuat menggunakan Streamlit untuk membantu pengguna mengestimasi jejak karbon pribadi mereka berdasarkan gaya hidup sehari-hari. Latar belakang proyek ini adalah untuk meningkatkan kesadaran akan dampak lingkungan dari aktivitas kita. Tujuan utamanya adalah memberikan feedback yang dipersonalisasi dan saran praktis menggunakan AI agar pengguna dapat mengambil langkah-langkah menuju gaya hidup yang lebih berkelanjutan.

## 2. Fitur-Fitur Utama

- **Kuesioner Interaktif:** 10 pertanyaan pilihan ganda yang mencakup aspek transportasi, diet, konsumsi energi, dan kebiasaan belanja.
- **Perhitungan Skor Otomatis:** Aplikasi secara otomatis menghitung skor jejak karbon berdasarkan bobot dari setiap jawaban.
- **Feedback Cerdas dari AI:** Terintegrasi dengan model AI melalui OpenRouter untuk memberikan analisis dan saran yang dipersonalisasi berdasarkan skor pengguna.
- **Antarmuka Modern:** Tampilan yang bersih dan modern dengan tema gelap kehijauan, lengkap dengan progress bar dan penyajian hasil yang menarik.

## 3. Cara Menjalankan di Lokal

1.  Pastikan Anda memiliki Python 3.8+ terinstal.
2.  Clone repositori ini atau unduh semua file dalam satu folder.
3.  Buat *virtual environment* (opsional, tapi disarankan):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Mac/Linux
    venv\Scripts\activate    # Untuk Windows
    ```
4.  Instal semua *dependency* yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```
5.  Siapkan API Key Anda di file `.streamlit/secrets.toml`:
    ```toml
    OPENROUTER_API_KEY = "sk-or-v1-..."
    ```
6.  Jalankan aplikasi Streamlit:
    ```bash
    streamlit run app.py
    ```
