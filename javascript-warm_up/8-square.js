#!/usr/bin/node
const process = require('process');
const line = process.argv;
if (isNaN(line[2]) || line[2] === undefined) {
  console.log('Missing size');
} else {
  const value = parseInt(line[2]);
  for (let i = value; i > 0; i--) {
    console.log('X'.repeat(value));
  }
}
