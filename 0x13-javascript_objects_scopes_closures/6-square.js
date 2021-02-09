#!/usr/bin/node

const Rectangle =  require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
  if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
  } else {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    }
  }
}
module.exports = Square;
