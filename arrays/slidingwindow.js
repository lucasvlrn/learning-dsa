function maximumLengthSubstring(s) {
  let l = 0;
  let r = 0;
  let _max = 1;
  counter = new Map();
  counter.set(s[0], 1);
  console.log(counter);

  while (r < s.length - 1) {
    r += 1;
    if (counter.get(s[r])) {
      counter.set(s[r], 1);
      console.log(counter);
    } else {
      counter.set(s[r], 1);
    }
  }

  while (counter.get(s[r] == 3)) {
    counter.set(s[l], 1);
    l += 1;
  }
  console.log(counter);
  _max = Math.max(_max, r - l + 1);
  return _max;
}

console.log(maximumLengthSubstring(["b", "c", "b", "b", "b", "c", "b", "a"]));


