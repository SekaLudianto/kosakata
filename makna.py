import json

input_file = "5huruf.json"
output_file = "5huruf_sederhana.js"

# === Baca file JSON sumber ===
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

result = []

# === Ekstraksi data penting ===
for kata, info in data.items():
    try:
        entri = info.get("data", {}).get("entri", [])
        if not entri:
            continue

        for e in entri:
            makna_list = e.get("makna", [])
            for m in makna_list:
                submakna = m.get("submakna", [])
                contoh = m.get("contoh", [])
                kelas = m.get("kelas", [])

                bahasa = ""
                for k in kelas:
                    if k.get("nama") not in ("Nomina", "Verba", "Adjektiva", "-"):
                        bahasa = k.get("nama")
                        break

                result.append({
                    "word": kata.upper(),
                    "arti": submakna[0] if submakna else "",
                    "contoh": contoh[0] if contoh else "",
                    "bahasa": bahasa
                })
    except Exception:
        continue

# === Simpan hasil ke format JavaScript ===
with open(output_file, "w", encoding="utf-8") as f:
    f.write("const DAFTAR_TEBAKAN_VALIDs = ")
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write(";")

print(f"Selesai. File disimpan ke {output_file}")