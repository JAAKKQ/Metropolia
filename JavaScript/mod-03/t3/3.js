'use strict';
const names = ['John', 'Paul', 'Jones'];

let string = ""
for (const name of names) {
    string += `<li>${name}</li>`
}

document.querySelector('#target').innerHTML = string;
