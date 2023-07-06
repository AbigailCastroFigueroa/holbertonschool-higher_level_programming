#!/usr/bin/node
const process = require('process');
const line = process.argv;

if (line.length <= 3) {
  console.log(0);
} else {
  const NewArray = [];
  let result = 0;
  for (let i = 2; i < line.length; i++) {
    NewArray.push(line[i]);
  }
  NewArray.sort(function (a, b) { return a - b; });
  for (let i = 0; i < NewArray.length - 1; i++) {
    result = NewArray[i];
  }
  console.log(result);
}
