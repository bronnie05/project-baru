

print("kalkulator BMI(BODY MASS INDEX)")
print("-------------------------------")

berat_badan = input("masukan berat badan (kg): ")
berat_badan = float(berat_badan)
tinggi_badan = input("masukan tinggi badan (m): ")
tinggi_badan = float(tinggi_badan)

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal["bawah"] = 18.5 * (tinggi_badan**2)
berat_badan_ideal["atas"] = 24.9 * (tinggi_badan**2)

print(berat_badan_ideal)

print(f"nilai bmi anda adalah: {bmi:.2f}")
print("berat badan ideal adalah 18,5-24.9 kg/m2")
print(f"berat badan ideal anda adalah: {berat_badan_ideal['bawah']:.2f} - {berat_badan_ideal['atas']:.2f} kg")