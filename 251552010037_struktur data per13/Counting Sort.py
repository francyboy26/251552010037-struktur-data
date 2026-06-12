def counting_sort(arr):
    print("input:", arr)
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    print("frekuensi (count array):")
    for i, c in enumerate(count):
        if c > 0:
            print(f"angka: {i}, kali: {c}")
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    print("output: (terurut)", sorted_arr)
    return sorted_arr

data = [5,3,8,4,2]
counting_sort(data)