#!/usr/bin/node
// this script gets the content of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.log('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(`Error: ${error.message}`);
      }
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
