#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const result = JSON.parse(body).results;
  for (const film of result) {
    for (const selectedCharacter of film.characters) {
      if (selectedCharacter.includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
