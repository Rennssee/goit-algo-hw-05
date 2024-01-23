def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1

        if arr[mid] == target:
            break  # Додали перевірку, якщо елемент знайдено, припиняємо цикл
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Перевіряємо, чи ліва межа виходить за межі масиву або є менше за шукане значення
    upper_bound = arr[left] if left < len(arr) and arr[left] >= target else None

    return iterations, upper_bound


# Тестування:
sorted_array = [0.1, 0.5, 1.2, 1.7, 2.0, 2.5, 3.1, 4.2, 5.0]
target_value = 2.0

result = binary_search(sorted_array, target_value)
iterations, upper_bound = result

print(f"Елемент {target_value} знайдено за {iterations} ітерацій.")
print(f"Верхня межа: {upper_bound}")
