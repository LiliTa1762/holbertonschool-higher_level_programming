#!/usr/bin/node

const urlPath = process.argv[2];
const request = require('request');

request(urlPath, { json: true }, (err, res, body) => {
  if (err) { console.log('code:', body.statusCode); }
  console.log('code:', res.statusCode);
});
