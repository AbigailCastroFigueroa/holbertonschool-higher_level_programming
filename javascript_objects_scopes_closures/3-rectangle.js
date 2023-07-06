#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (width, height) {
    for (let i = 0; i < this.height - 1; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
