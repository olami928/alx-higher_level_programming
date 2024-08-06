#!/usr/bin/node
// script reads and prints the content of a file

const fs = require('fs');
const filePath = process.argv[2];

function readFileContent (path) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}

readFileContent(filePath);
