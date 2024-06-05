#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

if (!url) {
  console.log('Please provide a URL to make a GET request.');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
