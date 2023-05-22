def quick_sort(arr, threshold=10):
    if len(arr) <= 1:
        return arr

    if len(arr) <= threshold:
        return insertion_sort(arr)

    pivot = arr[len(arr) // 2]
    left = []
    right = []
    equal = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    return quick_sort(left, threshold) + equal + quick_sort(right, threshold)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


import random

arr = random.sample(range(100), 20)
print("Исходный список:", arr)

for threshold in range(5, 15, 2):
    sorted_arr = quick_sort(arr, threshold)
    print(f"Список после сортировки с пределом раздела {threshold}:", sorted_arr)
