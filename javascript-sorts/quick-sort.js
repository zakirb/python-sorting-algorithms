function quick_sort(array) {
  if (array.length < 2) {
    return array
  }

  let lesser = []
  let greater = []
  let equal = []

  array.forEach((item) => {
    let pivot = array[0]
    if (item < pivot) {
      lesser.push(item)
    } else if (item > pivot) {
      greater.push(item)
    } else {
      equal.push(item)
    }
  })


  return quick_sort(lesser).concat(equal).concat(quick_sort(greater))
}


my_array = [1, 4, 5, 6, 345, 2, 34, 4, 5, 6]

console.log(quick_sort(my_array))
