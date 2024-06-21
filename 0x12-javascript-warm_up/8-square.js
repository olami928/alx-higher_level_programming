#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0], 10);
let i;

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
