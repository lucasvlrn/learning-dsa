function reverseWords_manual_cool(s) {
  let res = "";
  let l = 0;
  let r = 0;
  newArray = [];

  while (r < s.length) {
    if (s[r] != " ") {
      res += s[r];
      r += 1;
    } else {
      res += [s[r]];
      r += 1;
      l = r;
    }
  }
  res += " ";
  res += [s[r]];
  return;
}

//solução paia que tem no google
function reverseWords_manual(s) {
  let word = "";

  for (let i = s.length - 1; i >= 0; i--) {
    word += s[i];
  }
  return word;
}

// console.log(reverseWords_manual("Luc aas"));
console.log(reverseWords_manual_cool("Luc aas"));

//paia:
// let array = res.split(" ").reverse().join(" ");
