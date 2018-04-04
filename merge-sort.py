my_list = [413, 445, 403, 224, 157, 312, 785, 862, 602, 354, 90, 442, 458, 641, 595, 441, 661, 690, 963, 376, 840, 463, 514, 919, 789, 423, 81, 272, 46, 981, 375, 70,
 139, 955, 399, 179, 346, 369, 827, 171, 460, 982, 721, 631, 218, 200, 163, 510, 56, 30, 490, 320, 326, 327, 161, 586, 949, 244, 857, 750, 290, 716, 511, 573, 96, 340, 78, 800, 821, 417, 627,

847, 906, 672, 294, 279, 554, 709, 731, 344, 449, 790,
 231, 307, 39, 574, 566, 941, 72, 884, 763, 486, 66]

def merge(left_array, right_array):
    smallest_number = 0
    if len(right_array) == 0:
        return left_array

    if len(left_array) == 0:
        return right_array

    if left_array[0] <= right_array[0]:
        smallest_number = left_array.pop(0)
    else:
        smallest_number = right_array.pop(0)

    merged = merge(left_array, right_array)
    merged.insert(0, smallest_number)

    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_array = arr[:mid]
    right_array = arr[mid:]

    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)

    return merge(sorted_left_array, sorted_right_array)

print(merge_sort(my_list))
