#!/usr/bin/node

const argument = parseInt(process.argv[2]);

if (argument) {
  for (let i = 0; i < argument; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
