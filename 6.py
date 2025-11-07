import json
import os
import re

# daftar file input
input_files = [
    "kbbi_v_part1.json",
    "kbbi_v_part2.json",
    "kbbi_v_part3.json",
    "kbbi_v_part4.json"
]

# regex hanya huruf alfabet 6 karakter
pattern_6 = re.compile(r"^[a-zA-Z]{6}$")

word_list = set()

for file_name in input_files:
    if not os.path.exists(file_name):
        print(f"File tidak ditemukan: {file_name}")
        continue

    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

    for word in data.keys():
        if pattern_6.match(word):
            word_list.add(word.upper())

sorted_words = sorted(list(word_list))

# format JavaScript seperti contoh
js_output = "let wordList = [\n    "
js_output += ", ".join(f'"{w}"' for w in sorted_words)
js_output += ",\n];\n"

# simpan ke file
with open("6huruf.js", "w", encoding="utf-8") as f:
    f.write(js_output)

print(f"Selesai. {len(sorted_words)} kata 6 huruf disimpan di 6huruf.js")
