print("="*40)
print("     PROGRAM KATEGORI BMI (CDC & WHO)     ")
print("="*40)

berat = int(input("Masukkan berat (kg)   : "))
tinggi = int(input("Masukkan tinggi (cm) : "))

print("-"*40)

if berat <= 0 or tinggi <= 0:
    print("Input tidak valid: berat/tinggi harus > 0.")
elif not (50 <= tinggi <= 270):
    print("Input tidak valid: tinggi harus 50-270 cm.")
elif not (10 <= berat <= 500):
    print("Input tidak valid: berat harus 10-500 kg.")
else:
    bmi = berat / ((tinggi / 100) ** 2)


    if bmi < 18.5:
        if bmi < 16:
            kategori = "Underweight (Severe thinness)"
        elif bmi < 17:
            kategori = "Underweight (Moderate thinness)"
        else:
            kategori = "Underweight (Mild thinness)"
    elif bmi < 25:
        kategori = "Healthy (Normal)"
    elif bmi < 30:
        kategori = "Overweight"
    else:
        if bmi < 35:
            kategori = "Obesity Class I"
        elif bmi < 40:
            kategori = "Obesity Class II"
        else:
            kategori = "Obesity Class III"


    print(f"Berat Badan : {berat} kg")
    print(f"Tinggi      : {tinggi} cm")
    print(f"BMI         : {bmi:.2f}")
    print(f"Kategori    : {kategori}")

print("="*40)
print("Terima kasih telah memakai program ini")
print("="*40)


