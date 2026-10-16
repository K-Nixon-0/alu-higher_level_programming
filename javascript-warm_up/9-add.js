#!/usr/bin/node
function add (a, b) {
  return parseInt(a, 10) + parseInt(b, 10);
}
const args = process.argv.slice(2);
console.log(add(args[0], args[1]));
