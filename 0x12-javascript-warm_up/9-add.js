#!/usr/bin/node

const args = process.argv.slice(2);
function add (a, b) {
  const result = a + b;
  return (result);
}

if (args.length < 2) {
  console.log(NaN);
} else {
  const a = parseInt(args[0]);
  const b = parseInt(args[1]);

  if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
  } else {
    console.log(add(a, b));
  }
}
