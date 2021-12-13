#!/usr/bin/node
/*
   script that prints the addition of 2 integers
*/

function add (a, b) {
  return a + b;
}
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
const sum = add(num1, num2);
console.log(sum);
