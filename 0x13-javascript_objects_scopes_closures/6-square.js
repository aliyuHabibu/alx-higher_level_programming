#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let i, x;
    x = 0;
    while (x < this.size) {
      i = 0;
      while (i < this.size) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
        i++;
      }
      console.log();
      x++;
    }
  }
}
module.exports = Square;
