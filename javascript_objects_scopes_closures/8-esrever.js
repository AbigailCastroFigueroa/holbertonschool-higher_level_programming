#!/usr/bin/node
exports.esrever = function (list) {
  const ListLength = list.length;
  const newList = [];

  for (let i = ListLength -1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
