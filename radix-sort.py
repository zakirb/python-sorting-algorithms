my_arr = [413, 445, 403, 224, 157, 312, 785, 862, 602, 354, 90, 442, 458, 641, 595, 441, 661, 690, 963, 376, 840, 463, 514, 919, 789, 423, 81, 272, 46, 981, 375, 70, 139, 955, 399, 179, 346, 369, 827, 171, 460, 982, 721, 631, 218, 200, 163, 510, 56, 30, 490, 320, 326, 327, 161, 586, 949, 244, 857, 750, 290, 716, 511, 573, 96, 340, 78, 800, 821, 417, 627, 847, 906, 672, 294, 279, 554, 709, 731, 344, 449, 790, 231, 307, 39, 574, 566, 941]


def radix_sort(array):
    if len(array) < 2:
        return array

    number_of_digits = len(str(max(array)))

    for i in range(1, (number_of_digits + 1)):
        buckets = []
        for i in range(0, 10):
            buckets.append([])

      for j in range(len(array)):
        digit = ((array[j] % (10**i)) - (array[j] % (10**(i-1)))) // (10 **(i-1))
        buckets[digit].append(array[j])

      array = []
      for k in range(len(buckets)):
        array = array + buckets[k]
        
    print(array)

radix_sort(my_arr)
