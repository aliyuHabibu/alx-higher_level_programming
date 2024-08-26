#!/usr/bin/node

exports.converter = function (base) {
  if (base === 10) {
    return function (num) {
      return num.toString(base);
    };
  } else if (base === 16) {
    return function (num) {
      return num.toString(base);
    };
  }
};
