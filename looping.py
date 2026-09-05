# perulangan while-do
# Masalah 1: Countdown dengan Validasi
def countdown():
    while True:
        try:
            angka = int(input("Masukkan angka positif: "))
            if angka > 0:
                break
            else:
                print("Angka harus positif!")
        except ValueError:
            print("Input harus bilangan bulat!")
    
    while angka >= 0:
        print(angka, end=" ")
        angka -= 1
    print("Selesai!")

# Test
countdown()

# Masalah 1: Input Validasi dengan Repeat-Until
def input_positif():
    """Repeat-until pattern: minimal eksekusi sekali"""
    
    # Cara 1: While True dengan break
    while True:
        try:
            angka = int(input("Masukkan angka positif: "))
            if angka > 0:
                print(f"Terima kasih! Angka: {angka}")
                break
            print("Angka harus positif!")
        except ValueError:
            print("Input harus bilangan bulat!")

# Versi dengan do-while pattern lebih eksplisit
def input_positif_v2():
    """Do-while pattern dengan walrus operator"""
    while (invalid := True):
        try:
            angka = int(input("Masukkan angka positif: "))
            if angka > 0:
                print(f"Terima kasih! Angka: {angka}")
                invalid = False
            else:
                print("Angka harus positif!")
        except ValueError:
            print("Input harus bilangan bulat!")

# Test
print("=== Cara 1 ===")
input_positif()

print("\n=== Cara 2 ===")
input_positif_v2()