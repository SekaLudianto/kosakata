import json
import csv

# Nama file input/output
input_file = "kata.json"
output_file = "kata.csv"

# Baca file JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Pastikan data berupa list of dict
if not isinstance(data, list):
    raise ValueError("Format JSON tidak sesuai. Harus berupa array of objects.")

# Hilangkan duplikat berdasarkan "word"
unique_data = []
seen_words = set()

for item in data:
    word = item.get("word", "").strip().upper()  # normalisasi kapital dan spasi
    if word and word not in seen_words:
        seen_words.add(word)
        unique_data.append({
            "word": word,
            "arti": item.get("arti", "").strip(),
            "contoh": item.get("contoh", "").strip(),
            "bahasa": item.get("bahasa", "").strip()
        })

# Tentukan kolom CSV
fieldnames = ["word", "arti", "contoh", "bahasa"]

# Tulis ke CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(unique_data)

print(f"✅ Berhasil konversi {len(unique_data)} entri unik (dari {len(data)} total) ke '{output_file}'")
