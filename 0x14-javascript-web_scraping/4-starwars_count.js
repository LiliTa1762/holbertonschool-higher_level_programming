#!/usr/bin/node

const request = require('request');
const urlPath = process.argv[2];

request(urlPath, function (err, res, body) {
  if (err) { console.err(err); }
  const movies = JSON.parse(body).results;
  let i = 0;
  movies.forEach(movies => {
    const character = movies.characters;
    character.forEach(character => {
      if (character.includes('/18')) {
        i++;
      }
    });
  });
  console.log(i);
});
