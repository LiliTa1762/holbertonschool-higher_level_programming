#!/usr/bin/node

const urlPath = 'https://swapi-api.hbtn.io/api/films/';
const args = process.argv[2]; // Episode in command line
const request = require('request');

request(urlPath + args, function (err, res, body) {
  err && console.log(err);
  console.log(JSON.parse(body).title);
});

/* Tiene que devolver el title del número de la peli que le paso */
