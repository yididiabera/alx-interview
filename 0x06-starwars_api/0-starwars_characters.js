#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');

if (!movieId) {
    console.error('Usage: ./0-starwars_characters.js <movie_id>');
    process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character name by URL
function fetchCharacter(characterUrl) {
    return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode === 200) {
                resolve(JSON.parse(body).name);
            } else {
                reject(new Error('Request failed'));
            }
        });
    });
}

// Fetch movie details
request(url, async function (error, response, body) {
    if (error) {
        console.error(error);
        return;
    }
    if (response.statusCode === 200) {
        const characters = JSON.parse(body).characters;

        // Fetch character names in order
        for (const characterUrl of characters) {
            try {
                const characterName = await fetchCharacter(characterUrl);
                console.log(characterName);
            } catch (error) {
                console.error(error);
            }
        }
    } else {
        console.error('Failed to retrieve movie');
    }
});

