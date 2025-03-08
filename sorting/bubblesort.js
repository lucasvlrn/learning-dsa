function bubble_sort(arr) {
  for (let i = 0; i < arr.length; i++) {
    is_sorted = true;
    console.log(arr);
    for (let j = 0; j < arr.length - i; j++)
      if (arr[j] > arr[j + 1]) {
        is_sorted = false;
        let pot = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = pot;
      }
    if (is_sorted) break;
  }
  return arr;
}

// bubble_sort([5, 4, 3, 2, 1]);
// bubble_sort([1, 2, 3, 4, 5]);
// bubble_sort([1, 2, 5, 4, 3]);
