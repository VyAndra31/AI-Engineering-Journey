import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GEMINI_API_KEY")

# Masukkan token AQ, panggil fungsi bawaannya
client = genai.Client(api_key=TOKEN)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Hari ini enaknya makan apa ya?'
)

# Cetak hasilnya lewat .text
print("Dengan Library GenAI")
print(response.text)