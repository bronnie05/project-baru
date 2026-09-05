#match variabel:
#    case pola1:
#        aksi 1
#    case pola2:
#        aksi 2
#    case _:
#        default

# contoh penggunaan match case
while True:
    nilai = int(input("masukan nilai (0-100): "))
    match nilai:
        case n if 80 <= n <= 100:
            print("A")
        case n if 70 <= n < 80:
            print("B")
        case n if 60 <= n < 70:
            print("C")
        case n if 50 <= n < 60:
            print("D")
        case n if 0 <= n < 50:
            print("E")
        case _:
            print("nilai tidak valid")
    
    lagi = input("ingin mengulang (y/n)? ")
    if lagi.lower() != 'y':
        break
print("konversi hari ke dalam bahasa inggris")
def hari(hari_indo):
    match hari_indo.lower():
        case "senin":
            print("monday")
        case "selasa":
            print("tuesday")
        case "rabu":
            print("wednesday")
        case "kamis":
            print("thursday")
        case "jumat":
            print("friday")
        case "sabtu":
            print("saturday")
        case "minggu":
            print("sunday")
        case _:
            print("nama hari tidak ditemukan")

print(hari("senin"))