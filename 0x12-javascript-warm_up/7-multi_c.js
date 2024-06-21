#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0], 10);
let i;

if (isNaN(x)) {
  console.log('Missing number of occurences');
}
for (i = 0; i < x; i++) {
  console.log('C is fun');
}
