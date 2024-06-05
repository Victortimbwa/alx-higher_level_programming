#!/usr/bin/node

const fs = require('fs');

const [filePath, content] = process.argv.slice(2);

if (!filePath || !content) {
    console.log('Please provide both file path and content to write.');
    process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
        console.error(err);
    } else {
        console.log('Content has been written to the file successfully.');
    }
});