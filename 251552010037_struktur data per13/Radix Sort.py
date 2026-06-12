def counting_sort_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]
    
    print(f"hasil sort digit (exp={exp}):", arr)

def radix_sort(arr):
    print("input:", arr)
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_digit(arr, exp)
        exp *= 10
    print("output: (terurut)", arr)
    return arr

data = [5, 3, 8, 4, 2]
radix_sort(data)