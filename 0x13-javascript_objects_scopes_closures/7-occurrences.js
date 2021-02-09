#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let result = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      result += 1;
    }
  }
  return result;
};
