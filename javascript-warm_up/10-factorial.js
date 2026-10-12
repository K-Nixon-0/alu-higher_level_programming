#!/usr/bin/node
function factorialize(n) {
  if (n <= 1) return 1
  return n * factorialize(n - 1)
}

const args = process.argv.slice(2)
const num = parseInt(args[0], 10)
console.log(factorialize(num))