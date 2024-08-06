#!/usr/bin/node
// this script displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.log('Please provide a URL');
  process.exit(1);
}

function getStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

getStatusCode(url);
