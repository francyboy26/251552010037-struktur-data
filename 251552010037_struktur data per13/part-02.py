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