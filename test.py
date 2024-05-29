def bubble_sort(arr):
  def sort_pass(arr, n):
    if n == 1:
      return arr
    new_arr = arr[:]
    for i in range(n - 1):
      if new_arr[i] > new_arr[i + 1]:
        new_arr[i], new_arr[i + 1] = new_arr[i + 1], new_arr[i]
    return sort_pass(new_arr, n - 1)

  return sort_pass(arr, len(arr))

# Esempio di utilizzo
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
