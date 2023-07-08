#!/usr/bin/node
const words = process.argv.length - 2;
if (words === 0) {
  console.log('No Argument');
} else if (words === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
