#!/usr/bin/node
// this script writes a string to a file

const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

function writeFileContent (path, content) {
  fs.writeFile(path, content, 'utf8', (err) => {
    if (err) {
      console.log(`{err.message}`);
    }
  });
}

if (filePath && string) {
  writeFileContent(filePath, string);
} else {
  console.log('Provide a file path and string');
}
