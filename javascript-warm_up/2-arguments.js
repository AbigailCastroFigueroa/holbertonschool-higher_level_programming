#!/usr/bin/node
const process = require('process');
const line = process.argv;
const words = line.length;
if (words === 3) {
  console.log('Argument found');
} else if (words > 3) {
  console.log('Arguments found');
} else {
  console.log('No Argument');
}
