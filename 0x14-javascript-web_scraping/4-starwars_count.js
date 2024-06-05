#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body);

    const characterId = 18;
    const moviesWithWedge = films.results.filter((film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });
    console.log(`Number of movies with Wedge Antilles:${moviesWithWedge.lenght}`);
  } else {
    console.error('Failed to fetch data');
  }
});
