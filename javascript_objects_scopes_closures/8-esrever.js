#!/usr/bin/node
exports.esrever = function (list) {
  const ListLength = list.length - 1;
  const newList = [];

  for (let i = ListLength; i > 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
