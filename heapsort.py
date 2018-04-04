my_arr = [13, 12, 11, 1, 5, 3, 4, 2, 7]

def heapify(array, n, i):
  largest = i
  #right and left children
  l = i * 2 + 1
  r = i * 2 + 2

  if l < n and array[i] < array[l]:
    largest = l

  if r < n and array[largest] < array[r]:
    largest = r

  if largest != i:
    array[i], array[largest] = array[largest], array[i]
    heapify(array, n, largest)

def heap_sort(array):
  n = len(array)

  #max heap
  for i in range(n, -1, -1):
    heapify(array, n, i)

  for i in range(n-1, 0, -1):
    array[i], array[0] = array[0], array[i]
    heapify(array, i, 0)

  return array



print(heap_sort(my_arr))

#taken from the internet after 3 hours of attempting on my own
