#!/usr/bin/node

exports.nb0ccurences = function (list, searchElement) {
  let i = 0;
  let numOfOccur = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      numOfOccur++;
    }
    i++;
  }
  return numOfOccur;
};
