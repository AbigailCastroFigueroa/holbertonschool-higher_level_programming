#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const newFile = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const content = body;

  fs.writeFile(newFile, content, { encoding: 'utf8' }, (error) => {
    if (error) {
      console.error(error);
    }
  });
});
