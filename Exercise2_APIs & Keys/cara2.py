import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GEMINI_API_KEY")

# Tempelkan token AQ langsung di ujung URL endpoint Google
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={TOKEN}"

# Susun paket data JSON manual
payload = {
    "contents": [{
        "parts": [{"text": "Pilih angka random dari 1-100!"}]
    }]
}
headers = {"Content-Type": "application/json"}

# Kirim request lewat protokol internet POST
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Bongkar hasil dan ambil teks jawabannya
hasil_json = response.json()
jawaban_teks = hasil_json['candidates'][0]['content']['parts'][0]['text']

print("Dengan Raw HTTP")
print(jawaban_teks)