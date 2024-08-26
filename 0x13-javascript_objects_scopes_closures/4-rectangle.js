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
        process.stdout.write('X');
        x++;
      }
      console.log();
      i++;
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const wid = this.width;
    this.width = this.height;
    this.height = wid;
  }
}
module.exports = Rectangle;
