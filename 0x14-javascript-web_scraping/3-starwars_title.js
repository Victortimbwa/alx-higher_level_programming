#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide the movie ID as the first argument.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.log('Failed to retrieve data. Please check the movie ID.');
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const movieTitle = movieData.title;

  console.log(`The title of the Star Wars movie with ID ${movieId} is: ${movieTitle}`);
});
