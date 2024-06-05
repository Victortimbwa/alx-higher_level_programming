#!/usr/bin/node
const fs = require('fs');
const request = require('request');

if (process.argv.length !== 4) {
  console.error('Usage: node fetchAndStore.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      } else {
        console.log(`Successfully saved the contents of ${url} to ${filePath}`);
      }
    });
  }
});
