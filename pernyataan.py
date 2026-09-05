
while True:
    usia = int(input("Masukkan usia Anda: "))
    if 0 < usia < 12:
        print("anak-anak")
    elif 13 < usia < 17:
        print("remaja")
    elif 18 < usia < 50:
        print("dewasa")
    else:
        print("lansia")