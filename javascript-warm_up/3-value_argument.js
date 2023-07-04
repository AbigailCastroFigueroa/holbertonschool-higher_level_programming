#!/usr/bin/node
const process = require('process');
const line = process.argv;
if (line[2] !== undefined) {
  console.log(line[2]);
} else {
  console.log('No Argument');
}
