#!/usr/bin/node
/*
   script that prints x times C is fun
   Where x is the first argument of the script
*/
const number = parseInt(process.argv[2]);
if (number) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
