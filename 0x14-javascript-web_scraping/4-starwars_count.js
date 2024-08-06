#!/usr/bin/node
// this script prints the number of movies where the character
// "Wedge Antilles" is present

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Please provide the API URL');
  process.exit(1);
}

const wedgeAntillesId = 18;
const url = `https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach((film) => {
      if (film.characters.includes(url)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
