#!/usr/bin/node
const process = require('process');
const line = process.argv;
const convertedArg = parseInt(line[2]);
if (isNaN(convertedArg) === false) {
  console.log('My number: ' + convertedArg);
} else {
  console.log('Not a number');
}
