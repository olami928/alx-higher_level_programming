#!/usr/bin/node
// this script prints the title of a Star Wars movie where the episode
// numbers matches an integer

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie Id');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log(`Error: ${response.StatusCode}`);
  }
});
