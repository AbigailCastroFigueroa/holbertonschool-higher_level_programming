#!/usr/bin/node
const process = require('process');
const words = process.argv.lenght - 2;
if (words === 0) {
  console.log('No Argument');
} else if (words === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
