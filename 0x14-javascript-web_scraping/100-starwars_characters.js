#!/usr/bin/node
// this script prints all the characters of Star Wars film

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./100-starwars_characters.js <MOVIE ID>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach(cUrl => {
      request.get(cUrl, (cError, cResponse, cBody) => {
        if (cError) {
          console.log(`Error: ${cError.message}`);
          return;
        }

        if (cResponse.statusCode === 200) {
          const character = JSON.parse(cBody);
          console.log(character.name);
        } else {
          console.log(`Error: ${cResponse.statusCode}`);
        }
      });
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
