#!/usr/bin/node
const process = require('process');
const arguments = process.argv;
let amount_of_arguments = 0;
for (amount_of_arguments in arguments) {
    amount_of_arguments++;
} 
if (arguments != null && amount_of_arguments > 2){
    for (let i = 2; i <= amount_of_arguments - 1; i++) {
        console.log(arguments[i]);
    }
}
else {
    console.log('No Argument');
}
