#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let moviesWithCharacter = 0;

    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        moviesWithCharacter++;
      }
    });

    console.log(moviesWithCharacter);
  } else {
    console.log('Failed to fetch data. Status code: ' + response.statusCode);
  }
});
