#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');

if (!movieId) {
  console.error('Usage: ./starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    
    function fetchCharacter(characterUrl) {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          }
          if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(new Error('Failed to fetch character'));
          }
        });
      });
    }

    Promise.all(characters.map(fetchCharacter))
      .then((characterNames) => {
        characterNames.forEach(name => console.log(name));
      })
      .catch((error) => console.error('Error fetching characters:', error));
  } else {
    console.error('Failed to fetch movie data');
  }
});

