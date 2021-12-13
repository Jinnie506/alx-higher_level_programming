#!/usr/bin/node
/*
   script that prints 3 lines but by using an array of string and a loop
*/
const args = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let line;
for (line of args) {
  console.log(line);
}
