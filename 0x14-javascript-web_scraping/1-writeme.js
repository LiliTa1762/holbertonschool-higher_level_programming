#!/usr/bin/node

const filePath = process.argv[2];
const strToW = process.argv[3];
const fs = require('fs');

fs.writeFile(filePath, strToW, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
