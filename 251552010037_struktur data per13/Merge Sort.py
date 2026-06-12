def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        Left = arr[:mid]
        Right = arr[mid:]

        print(f"splitting: {arr}")
        merge_sort(Left)
        merge_sort(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1
        
        print(f"merged: {arr}")

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)