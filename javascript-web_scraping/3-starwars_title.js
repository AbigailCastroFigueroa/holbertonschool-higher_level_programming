#!/usr/bin/node
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
const ApiRequest = url + movieId;
const request = require('request');
request(ApiRequest, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
