# contoh list
my_list = [1, 2, 3, 4, 5]

#list bersifat berurutan, mutable, dan boleh duplikat
mut = [1, 2, 3]
mut[0] = "satu"
print(mut)

#menempellkan list dengan list
list1 = ["a", "b", "c"]
list2 =[4, 5, 6]
list_baru = list1 + list2
print(list_baru)

# dapat mengalikan list dengan integer
#nanti hasilnya berulanngn kali
list2 * 3
print(list2 * 3)

# list methode adalah fungsi2 yang ada pada tipe data list
A = [1, 2, 3, 4, 5]
# 1. append()
A.append(6)
print(A)

# 2. sort()
A.sort(reverse=True) # reverse itu membalikan urutan
print(A)

# 3. clear() menghapus semua anggota list
A.clear()
print(A)

# 4. pop() mengembalikan dan menghapus list dengan indeks tertentu
A = [1, 2, 3, 4, 5]
print(A.pop(2)) # menghapus indeks ke 2
print(A)

# Build-in function pada list
# 1. list() mengubah tipe data lain menjadi list
b = (1,2)
list_b = list(b)
print(list_b)
# 2. max() menga,bil nilai maksimal
c = [1, 2, 3, 4, 5]
print(max(c))

# 3. min() mengambil nilai minimal
print(min(c))
