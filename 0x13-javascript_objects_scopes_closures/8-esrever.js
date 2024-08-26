#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  let i = list.length;
  let index = 0;
  while (i >= 1) {
    myList[index] = list[i - 1];
    index++;
    i--;
  }
  return myList;
};
