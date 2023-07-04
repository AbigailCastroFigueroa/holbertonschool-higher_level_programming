#!/usr/bin/node 
const process = require('process');
const arguments = process.argv;
let amount_of_arguments = arguments.length
if (amount_of_arguments === 3) {
    console.log('Argument found');
}
else if (amount_of_arguments > 3) {
    console.log('Arguments found');
}
else {
    console.log('No Argument');
}