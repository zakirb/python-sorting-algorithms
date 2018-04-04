def quick_sort(array):
    if len(array) < 2:
        return array

    lesser = []
    greater = []
    equal = []

    for i in array:
        pivot = array[0]
        if i < pivot:
            lesser.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)

    return quick_sort(lesser) + equal + quick_sort(greater)

my_list = [1, 4, 5, 6, 345, 2, 34, 4, 5, 6]

print(quick_sort(my_list))
