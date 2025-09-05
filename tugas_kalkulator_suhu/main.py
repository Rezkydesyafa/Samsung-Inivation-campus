from utils import (
    celcius_to_fahrenheit,
    celcius_to_kelvin,
    fahrenheit_to_celcius,
    fahrenheit_to_kelvin,
    kelvin_to_celcius,
    kelvin_to_fahrenheit
)

def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."

    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."

    if dari == ke:
        return nilai

    match (dari, ke):
        case ("c", "f"):
            return celcius_to_fahrenheit(nilai)
        case ("c", "k"):
            return celcius_to_kelvin(nilai)
        case ("f", "c"):
            return fahrenheit_to_celcius(nilai)
        case ("f", "k"):
            return fahrenheit_to_kelvin(nilai)
        case ("k", "c"):
            return kelvin_to_celcius(nilai)
        case ("k", "f"):
            return kelvin_to_fahrenheit(nilai)


print("=== KONVERSI SUHU ===")
try:
    nilai = int(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ")
    tujuan = input("ke satuan (C/F/K): ")

    hasil = konversi_suhu(nilai, dari, tujuan)


    print(f"Hasil: {nilai}°{dari.upper()} = {hasil:.2f}°{tujuan.upper()}")

except ValueError:
    print("Error: Nilai suhu harus berupa angka.")
