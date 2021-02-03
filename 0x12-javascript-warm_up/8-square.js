#!/usr/bin/node

const argument = parseInt(process.argv[2]);

if (argument) {
    for (let x = 0; x < argument; x++) {
	    console.log('X'.repeat(argument));
	}
} else {
    console.log('Missing size');
}
