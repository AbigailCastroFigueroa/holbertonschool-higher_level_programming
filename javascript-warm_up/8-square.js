#!/usr/bin/node
const process = require('process');
const line = process.argv;
if (isNaN(line[2]) || line[2] === undefined) {
  console.log('Missing size');
} else {
  value = parseInt(line[2]);
  for (let i = value; 0 < i; i--) {
    console.log('X'.repeat(value));
  }      
}
