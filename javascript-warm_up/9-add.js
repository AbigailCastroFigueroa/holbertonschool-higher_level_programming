#!/usr/bin/node
const process = require('process');
const line = process.argv;
const first = parseInt(line[2]);
const second = parseInt(line[3]);

function add (a, b) {
  return a + b;
}

if (line.length < 2) {
  console.log('NaN');
} else if (isNaN(second) || second === undefined) {
  console.log('NaN');
} else if (line.length < 3) {
  console.log('NaN');
} else {
  console.log(add(first, second));
}
