import pandas as pd 
import matplotlib.pyplot as plt 

# data penjualan selama 6 hari pertama (10 baris)
data = [
    {"tanggal": "2025-07-01", "warna": "merah", "ukuran": "M", "jumlah": 2, "harga": 25000},
    {"tanggal": "2025-07-01", "warna": "putih", "ukuran": "L", "jumlah": 1, "harga": 30000},
    {"tanggal": "2025-07-02", "warna": "hitam", "ukuran": "XL", "jumlah": 3, "harga": 35000},
    {"tanggal": "2025-07-02", "warna": "merah", "ukuran": "S", "jumlah": 4, "harga": 20000},
    {"tanggal": "2025-07-03", "warna": "putih", "ukuran": "M", "jumlah": 2, "harga": 25000},
    {"tanggal": "2025-07-03", "warna": "hitam", "ukuran": "L", "jumlah": 1, "harga": 30000},
    {"tanggal": "2025-07-04", "warna": "merah", "ukuran": "XL", "jumlah": 1, "harga": 35000},
    {"tanggal": "2025-07-04", "warna": "putih", "ukuran": "S", "jumlah": 3, "harga": 20000},
    {"tanggal": "2025-07-05", "warna": "hitam", "ukuran": "S", "jumlah": 2, "harga": 20000},
    {"tanggal": "2025-07-05", "warna": "merah", "ukuran": "L", "jumlah": 3, "harga": 30000},
]

df = pd.DataFrame(data)
df["total"] = df["jumlah"] * df["harga"]

total_penjualan = df["total"].sum()

warna_order = ["merah", "putih", "hitam"]
warna_terjual = df.groupby("warna")["jumlah"].sum().reindex(warna_order)
total_kaos = warna_terjual.sum()

probalitas = (warna_terjual/ total_kaos) * 100

print("Total penjualan selama 6 hari: rp {:,.0f}".format(total_penjualan))
print("\nProbabilitas warna paling sering di beli:")
for warna, prob in probalitas.items():
    print(f"{warna}: {prob:.2f}%")

warna_grafik = ["merah", "putih", "hitam"]
plt.figure(figsize=(8, 5))
plt.bar(probalitas.index, probalitas.values, color=warna_grafik, edgecolor='grey')
plt.title("Probabilitas pembelian kaos per warna (6 hari)")
plt.ylabel("presentase (%)")
plt.xlabel("warna kaos")
plt.ylim(0, 50)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

warna_data = list(zip(warna_terjual.index, warna_terjual.values))

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

sorted_warna = bubble_sort(warna_data)

print("\nhasil pengurutan (bubble sort) berdasarkan jumlah terbanyak:")
for warna, jumlah in sorted_warna:
    print(f"{warna}, : {jumlah} kaos")