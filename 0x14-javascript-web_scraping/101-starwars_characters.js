#!/usr/bin/node
// this script prints all the characters of a film in Star Wars

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
    console.log('Usage: ./101-starwars_characters.js <Movie ID>');
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

        let completedRequests = 0;

        characters.forEach(characterUrl => {
            request.get(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error(`Error: ${charError.message}`);
                    return;
                }

                if (charResponse.statusCode === 200) {
                    const character = JSON.parse(charBody);
                    console.log(character.name);
                } else {
                    console.log(`Error: ${charResponse.statusCode}`);
                }

                completedRequests++;

                if (completedRequests === characters.length) {
                }
            });
        });
    } else {
        console.log(`Error: ${response.statusCode}`);
    }
});

