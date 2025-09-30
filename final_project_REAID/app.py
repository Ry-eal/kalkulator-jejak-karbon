# app.py

import streamlit as st
import time # Kita akan gunakan untuk simulasi loading
from question import QUESTIONS
from core import CarbonFootprintCalculator

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Kalkulator Jejak Karbon",
    layout="centered", # 'centered' atau 'wide'
    initial_sidebar_state="auto"
)

# --- FUNGSI BANTUAN ---
# Fungsi untuk menerapkan CSS kustom (jika diperlukan di masa depan)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css("style.css") # Jika Anda ingin menambahkan file CSS terpisah

# --- INISIALISASI APLIKASI ---
calculator = CarbonFootprintCalculator(QUESTIONS)
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# --- UI: HEADER ---
# Menggunakan kolom untuk layout yang lebih menarik
# Versi baru
st.title("🌍 Kalkulator Jejak Karbon") # <-- Ikon langsung ditambahkan di sini
st.caption("Ukur & Pahami Dampak Lingkungan Anda")

st.divider()

st.write(
    "Selamat datang! Jawab 10 pertanyaan singkat ini untuk mendapatkan estimasi "
    "jejak karbon pribadi Anda, lengkap dengan saran cerdas dari AI."
)

# --- UI: FORM KUESIONER ---
# Menggunakan st.form untuk mengumpulkan semua jawaban sebelum diproses
with st.form(key='carbon_form'):
    # Loop untuk menampilkan semua pertanyaan
    for i, q in enumerate(QUESTIONS):
        st.subheader(f"Pertanyaan {i+1}: {q['question']}")
        
        # st.radio dibuat di dalam form
        answer = st.radio(
            label="Pilih satu:",
            options=q['options'].keys(),
            format_func=lambda key: q['options'][key], # Menampilkan teks opsi, bukan key 'A'/'B'
            key=f"q_{i}",
            label_visibility="collapsed",
            index=None
        )
        st.session_state.user_answers[i] = answer
        st.write("") # Memberi sedikit spasi

    # Tombol submit untuk form
    submitted = st.form_submit_button("Analisis Jejak Karbon Saya Sekarang!", type="primary")


# --- LOGIKA SETELAH SUBMIT ---
if submitted:
    # Validasi: Cek apakah semua pertanyaan sudah dijawab
    if None in st.session_state.user_answers.values():
        st.error("Oops! Sepertinya ada pertanyaan yang terlewat. Mohon jawab semuanya.")
    else:
        # Pesan loading yang kreatif
        loading_messages = [
            "Menghitung emisi dari perjalanan Anda...",
            "Menganalisis pola konsumsi Anda...",
            "Meminta saran dari pakar lingkungan (AI)...",
            "Menyiapkan laporan Anda..."
        ]
        progress_bar = st.progress(0, text=loading_messages[0])
        
        for i, msg in enumerate(loading_messages):
            time.sleep(1) # Simulasi proses
            progress_bar.progress((i + 1) * 25, text=msg)
        
        # Proses data
        for index, answer_key in st.session_state.user_answers.items():
            calculator.record_answer(index, answer_key)

        final_score = calculator.calculate_score()
        ai_feedback = calculator.get_ai_feedback(
            api_key=st.secrets["OPENROUTER_API_KEY"], 
            final_score=final_score
        )
        
        progress_bar.empty() # Menghilangkan progress bar setelah selesai

        # --- UI: TAMPILAN HASIL MODERN ---
        st.header("Laporan Jejak Karbon Anda", divider="rainbow")

        # Menentukan kategori & visualisasi
        if final_score <= 40:
            category = "Rendah"
            color = "green"
        elif final_score <= 70:
            category = "Sedang"
            color = "orange"
        else:
            category = "Tinggi"
            color = "red"

        # Skor dalam progress bar
        st.write(f"Total Skor Anda: **{final_score}** (Kategori: **{category}**)")
        st.progress(final_score, text=f"{final_score}/100")
        
        st.markdown(f"Skor Anda masuk dalam kategori **:{color}[{category}]**. Ini menunjukkan gambaran awal dari dampak gaya hidup Anda terhadap lingkungan.")

        # Feedback AI dalam expander
        with st.expander("Lihat Analisis dan Saran Cerdas dari AI", expanded=True):
            st.info(ai_feedback)

        st.success("Terima kasih telah berpartisipasi! Langkah kecil hari ini bisa menciptakan perubahan besar untuk bumi esok hari.")

# --- UI: FOOTER ---
st.divider()
st.markdown(
    """
    <div style="text-align: center; font-size: 0.9em; color: grey;">
        RYEAL AI.<br>
        Proyek Akhir oleh Ryo Alesandro.
    </div>
    """,
    unsafe_allow_html=True
)