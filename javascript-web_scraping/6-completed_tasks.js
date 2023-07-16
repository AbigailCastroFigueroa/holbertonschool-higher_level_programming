#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dictionary = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const result = JSON.parse(body);
  result.forEach(task => {
    if (task.completed) {
      if (task.userId in dictionary) {
        dictionary[task.userId]++;
      } else {
        dictionary[task.userId] = 1;
      }
    }
  });
  console.log(dictionary);
});
