#!/usr/bin/node

let myArgs = process.argv[2];

if (myArgs === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs);
}
