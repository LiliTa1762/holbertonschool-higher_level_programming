#!/usr/bin/node

function add(a, b) {
    a = parseInt(process.argv[2]);
    b = parseInt(process.argv[3]);

    if (a !== null && b !== null) {
	console.log(a + b);
    }
    else {
	console.log('NaN');
    }
}
add(process.argv[2], process.argv[3]);
