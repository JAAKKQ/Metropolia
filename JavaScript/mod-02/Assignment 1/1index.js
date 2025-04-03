'use strict';

let list = []

for (let i = 1; i <= 5; i++) {
    list.push(parseInt(prompt(`Give me a number for index ${i}/5`)))
}

for (let i = list.length-1; i >= 0; i--) {
    console.log(list[i])
}