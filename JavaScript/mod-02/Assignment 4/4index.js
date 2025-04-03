'use strict';

let list = []
for (let i = 1; true; i++) {
    list.push(parseInt(prompt(`Give me a number.`)))
    console.log(list[-1])
    if (list[list.length-1] === 0) {
        break
    }
}

list.sort((a, b) => b - a)

for (let name of list) {
    document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${name}</li>`);
}