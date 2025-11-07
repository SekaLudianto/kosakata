# split_kbbi_by_length.py
import json
import os
import re
from collections import defaultdict

# daftar file input (ubah sesuai kebutuhan)
input_files = [
    "kbbi_v_part1.json",
    "kbbi_v_part2.json",
    "kbbi_v_part3.json",
    "kbbi_v_part4.json"
]

# rentang panjang kata yang diinginkan (ubah atau perluas bila perlu)
min_len = 7
max_len = 11

# buat pola regex untuk huruf alfabet saja
patterns = {n: re.compile(rf"^[a-zA-Z]{{{n}}}$") for n in range(min_len, max_len + 1)}

# wadah hasil: tiap panjang menyimpan dict word -> content (sama struktur dengan input)
word_groups = {n: {} for n in range(min_len, max_len + 1)}
skipped = 0
total_seen = 0

for file_name in input_files:
    if not os.path.exists(file_name):
        print(f"File tidak ditemukan: {file_name}  (lewati)")
        continue

    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        print(f"Format file {file_name} tidak diharapkan (bukan object/dict). Lewati.")
        continue

    for word, content in data.items():
        total_seen += 1
        placed = False
        for n, pattern in patterns.items():
            if pattern.match(word):
                # simpan persis seperti input (tanpa mengubah case)
                word_groups[n][word] = content
                placed = True
                break
        if not placed:
            skipped += 1

# Simpan tiap file output
for n in range(min_len, max_len + 1):
    out_file = f"{n}huruf.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(word_groups[n], f, ensure_ascii=False, indent=2)
    print(f"Selesai: {len(word_groups[n])} kata {n} huruf disimpan ke {out_file}")

print(f"Total kata diproses: {total_seen}. Kata yang tidak cocok pola {min_len}-{max_len} huruf: {skipped}.")