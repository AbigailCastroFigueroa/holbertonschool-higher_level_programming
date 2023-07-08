#!/usr/bin/node
const process = require('process');
const line = process.argv;
const words = line.length;
if (words < 3) {
  console.log('No Argument');
} else if (words === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
