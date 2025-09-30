# core.py

# Impor library baru
from openai import OpenAI

class CarbonFootprintCalculator:
    def __init__(self, questions_data):
        self.questions = questions_data
        self.answers = {}

    def record_answer(self, question_index, answer_key):
        self.answers[question_index] = answer_key

    def calculate_score(self):
        total_score = 0
        if not self.answers:
            return 0
        for index, answer_key in self.answers.items():
            question = self.questions[index]
            total_score += question["weights"][answer_key]
        return total_score

    # --- INI FUNGSI YANG KITA UBAH TOTAL ---
    def get_ai_feedback(self, api_key, final_score):
        """Memberikan feedback menggunakan model dari OpenRouter."""
        
        try:
            # Membuat koneksi ke OpenRouter
            client = OpenAI(
              base_url="https://openrouter.ai/api/v1",
              api_key=api_key,
            )

            # Menentukan kategori skor
            if final_score <= 10:
                category = "Sangat Rendah"
            elif final_score <= 20:
                category = "Rendah"
            elif final_score <= 30:
                category = "Sedang"
            else:
                category = "Tinggi"
            
            # Membuat prompt untuk AI
            prompt_pesan = f"""
            Anda adalah seorang ahli lingkungan yang ramah.
            Seorang pengguna telah menyelesaikan kuesioner jejak karbon dan mendapatkan skor {final_score}, yang masuk dalam kategori '{category}'.
            Berikan feedback yang positif dan membangun dalam satu paragraf (sekitar 3-4 kalimat).
            Jelaskan secara singkat apa arti kategori skor tersebut dan berikan 2 saran praktis yang mudah dilakukan untuk mengurangi jejak karbon.
            Gunakan gaya bahasa yang memotivasi dan jawab dalam Bahasa Indonesia.
            """

            # Mengirim permintaan ke API OpenRouter
            response = client.chat.completions.create(
              model="google/gemini-2.0-flash-exp:free", # Anda bisa ganti model lain dari OpenRouter
              messages=[
                {"role": "system", "content": "Anda adalah asisten ahli lingkungan yang ramah."},
                {"role": "user", "content": prompt_pesan},
              ]
            )
            
            # Mengambil hasil dari respons
            return response.choices[0].message.content

        except Exception as e:
            return f"Terjadi error saat menghubungi OpenRouter: {e}"