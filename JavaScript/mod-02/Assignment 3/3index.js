'use strict';

let list = []
for (let i = 1; i <= 6; i++) {
    list.push(prompt(`Give me the name of dog number ${i}/6`))
}

list.reverse()

for (let name of list) {
    document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${name}</li>`);
}