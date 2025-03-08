function recursev(n, limit) {
  if (n <= limit) {
    console.log(n);
    n += 1;
    recursev(n, limit);
  }
}

recursev(1, 100);
