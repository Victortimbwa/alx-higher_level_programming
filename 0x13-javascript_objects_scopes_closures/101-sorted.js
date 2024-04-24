#!/usr/bin/node

const { dict } = require('./101-data');

// Create a new dictionary to store user ids by occurrence
const newUserDict = {};

// Iterate through the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // If occurrences is not a key in newUserDict, create an empty array for it
  if (!newUserDict[occurrences]) {
    newUserDict[occurrences] = [];
  }

  // Push the current userId to the array corresponding to the occurrences
  newUserDict[occurrences].push(userId);
}

console.log(newUserDict);
