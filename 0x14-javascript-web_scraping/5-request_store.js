#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const urlPath = process.argv[2];
const storePath = process.argv[3];

request.get(urlPath, function (err, res, body) {
  if (err) console.log(err);
  fs.writeFile(storePath, body, 'utf-8', (err) => {
    if (err) console.log(err);
  });
});
