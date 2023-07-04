#!/usr/bin/node
const process = require('process');
const line = process.argv;
if (line[2] !== undefined) {
  for (let i = parseInt(line[2]); i > 0; i--) {
    console.log('C is fun');
  }
} else if (line[2] === undefined) {
  console.log('Missing number of occurrences');
}
