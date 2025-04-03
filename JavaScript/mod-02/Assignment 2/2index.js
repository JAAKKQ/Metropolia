'use strict';

const number = parseInt(prompt("Give me a number of participants."))
let list = []
for (let i = 1; i <= number; i++) {
    list.push(prompt(`Give me the name of participant number ${i}`))
}

list.sort()

for (let name of list) {
    document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${name}</li>`);
}