#!/usr/bin/node

const urlPath = 'https://swapi-api.hbtn.io/api/films';
let args = process.argv[2];
const request = require('request');

request(urlPath, { json: true }, (err, res, body) => {
  console.log(body.results[args].title);
});
