#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');

if (!movieId) {
    console.error('Usage: ./0-starwars_characters.js <movie_id>');
    process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, async function (error, response, body) {
    if (error) {
        console.error(error);
    }
    if (response.statusCode === 200) {
        const characters = JSON.parse(body).characters;
        function fetchCharacter(character) {
            return new Promise((resolve, reject) => {
                request(character, (error, response, body) => {
                    if (error) {
                        reject(error);
                    }
                    if (response.statusCode === 200) {
                        resolve(JSON.parse(body).name);
                    }
                    reject(new Error('Request failed'));
                })
            })
        }
        Promise.all(characters.map(fetchCharacter))
            .then((characters) => {
                characters.forEach((character) => console.log(character));
            })
            .catch((error) => console.error(error));
    }
});
