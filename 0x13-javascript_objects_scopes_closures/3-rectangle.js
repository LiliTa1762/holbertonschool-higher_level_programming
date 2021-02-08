#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return 'Rectangle {}';
    }
  }

  print () {
    const stringx = 'X';
    while (this.height > 0) {
      console.log(stringx.repeat(this.width));
      this.height--;
    }
  }
};
