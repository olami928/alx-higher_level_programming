#!/usr/bin/node

const args = process.argv.slice(2);

function findSecondBiggest (args) {
  if (args.length < 2) {
    return 0;
  }

  let max = -Infinity;
  let secondMax = -Infinity;
  let i;

  for (i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }
  return secondMax;
}

console.log(findSecondBiggest(args));
