a = ' '
for (let i = 1; i <= 8; i = i + 1) {
  for (let j = 1; j <= 8; j = j + 1 ) {
    if (j % 2 == 0) {
      a += ' '
    } else a += '#'
  }
    if (i % 2 == 0) {
      a += '\n '
    } else a+= '\n'
    
}
console.log(a)