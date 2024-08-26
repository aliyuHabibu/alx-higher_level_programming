#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, x;
    i = 0;
    while (i < this.height) {
      x = 0;
      while (x < this.width) {
        // console.log('X\r');
        process.stdout.write('X');
        x++;
      }
      console.log();
      i++;
    }
  }
}
module.exports = Rectangle;
