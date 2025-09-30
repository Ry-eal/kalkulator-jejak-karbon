# question.py

QUESTIONS = [
    {
        "question": "Transportasi utama apa yang Anda gunakan untuk bepergian setiap hari?",
        "options": {
            "A": "Berjalan kaki atau bersepeda",
            "B": "Transportasi umum (bus, kereta)",
            "C": "Sepeda motor",
            "D": "Mobil pribadi"
        },
        "weights": {
            "A": 1,
            "B": 3,
            "C": 5,
            "D": 10
        }
    },
    {
        "question": "Seberapa sering Anda mengonsumsi daging merah (sapi, domba) dalam seminggu?",
        "options": {
            "A": "Tidak pernah / vegetarian",
            "B": "1-2 kali seminggu",
            "C": "3-5 kali seminggu",
            "D": "Hampir setiap hari"
        },
        "weights": {
            "A": 1,
            "B": 4,
            "C": 7,
            "D": 10
        }
    },
    {
        "question": "Bagaimana Anda mengatur suhu di rumah Anda?",
        "options": {
            "A": "Jarang menggunakan AC/pemanas, lebih sering membuka jendela",
            "B": "Menggunakan kipas angin saat diperlukan",
            "C": "Menggunakan AC/pemanas beberapa jam sehari",
            "D": "AC/pemanas menyala hampir sepanjang hari"
        },
        "weights": {
            "A": 1,
            "B": 2,
            "C": 6,
            "D": 9
        }
    },
    {
        "question": "Seberapa sering Anda membeli produk baru (pakaian, elektronik, dll) daripada memperbaiki yang lama?",
        "options": {
            "A": "Saya selalu berusaha memperbaiki dulu",
            "B": "Kadang memperbaiki, kadang beli baru",
            "C": "Seringnya membeli baru",
            "D": "Selalu membeli baru"
        },
        "weights": {
            "A": 2,
            "B": 4,
            "C": 6,
            "D": 8
        }
    },
    {
        "question": "Bagaimana Anda mengelola sampah di rumah?",
        "options": {
            "A": "Memilah sampah organik dan anorganik untuk didaur ulang",
            "B": "Membuang semua sampah menjadi satu",
            "C": "Kadang-kadang memilah jika sempat",
            "D": "Saya membuat kompos dari sampah organik"
        },
        "weights": {
            "A": 3,
            "B": 8,
            "C": 6,
            "D": 1 # Membuat kompos sangat baik
        }
    },
    {
        "question": "Saat berbelanja, apa yang biasa Anda gunakan untuk membawa barang?",
        "options": {
            "A": "Selalu membawa tas belanja sendiri",
            "B": "Kadang membawa tas sendiri, kadang tidak",
            "C": "Menggunakan kantong plastik yang disediakan toko",
            "D": "Meminta kantong plastik ganda agar lebih kuat"
        },
        "weights": {
            "A": 1,
            "B": 3,
            "C": 6,
            "D": 8
        }
    },
    {
        "question": "Seberapa sering Anda melakukan perjalanan dengan pesawat dalam setahun?",
        "options": {
            "A": "Tidak pernah",
            "B": "1-2 kali (pulang-pergi)",
            "C": "3-5 kali (pulang-pergi)",
            "D": "Lebih dari 5 kali (pulang-pergi)"
        },
        "weights": {
            "A": 1,
            "B": 5,
            "C": 8,
            "D": 10
        }
    },
    {
        "question": "Jenis makanan apa yang paling sering Anda buang?",
        "options": {
            "A": "Sangat jarang membuang makanan",
            "B": "Sisa sayuran atau buah",
            "C": "Sisa makanan matang (nasi, lauk)",
            "D": "Sering membuang makanan yang sudah kedaluwarsa"
        },
        "weights": {
            "A": 1,
            "B": 3,
            "C": 5,
            "D": 7
        }
    },
    {
        "question": "Dari mana sumber listrik utama di rumah Anda?",
        "options": {
            "A": "Panel surya atau sumber terbarukan lainnya",
            "B": "Listrik dari PLN (sumber campuran)",
            "C": "Generator pribadi berbahan bakar fosil",
            "D": "Saya tidak tahu"
        },
        "weights": {
            "A": 1,
            "B": 7,
            "C": 10,
            "D": 7 # Asumsikan sama dengan PLN jika tidak tahu
        }
    },
    {
        "question": "Seberapa sering Anda membeli air minum dalam kemasan botol plastik?",
        "options": {
            "A": "Tidak pernah, saya pakai filter air atau galon isi ulang",
            "B": "Kadang-kadang jika bepergian",
            "C": "Cukup sering, beberapa kali seminggu",
            "D": "Hampir setiap hari"
        },
        "weights": {
            "A": 1,
            "B": 3,
            "C": 6,
            "D": 8
        }
    }
]