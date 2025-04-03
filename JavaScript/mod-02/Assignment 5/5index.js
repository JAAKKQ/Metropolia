'use strict';

let list = []
for (let i = 1; true; i++) {
    const number = parseInt(prompt(`Give me a number.`))

    if (list.includes(number)) {
        alert("Number was already given.")
        break
    } else {
        list.push(number)
    }
}

list.sort((a, b) => a - b)

for (let name of list) {
    document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${name}</li>`);
}