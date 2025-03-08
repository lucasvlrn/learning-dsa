function binary_search(nums, n) {
  low = 0;
  hi = nums.length;

  while (low < hi) {
    mid = (low + hi) / 2;
    if (nums[mid] == n) return mid;
    else if (nums[mid] < n) low = mid + 1;
    else hi = mid;
    return "Não encontrado em" + nums;
  }
}

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(binary_search(arr, 6));
