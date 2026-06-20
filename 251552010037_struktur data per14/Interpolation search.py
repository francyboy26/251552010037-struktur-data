def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= key <= arr[high]:
       
       pas = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

       if pas < 0 or pas >= len(arr):
           return -1
       
    if arr[pas] == key:
        return pas
    elif arr[pas] < key:
        low = pas + 1
    else:
        high = pas - 1
    return -1

data = [1, 2, 3, 4, 5]
print("array saat ini:", data)

cari = int(input("Masukkan angka yang ingin dicari: "))

hasil = interpolation_search(data, cari)

if hasil != -1:
    print("Angka ditemukan pada indeks:", hasil)
else:
    print("Angka tidak ditemukan dalam array.")