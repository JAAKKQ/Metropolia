'use strict';

function roll(max) {
    return Math.floor(Math.random() * max + 1)
}

const max = parseInt(prompt("What is the maximum number on the dice?"))

for (let i = 1; true; i++) {
    const dice = roll(max)
    if (dice === max) {
        document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${dice}</li>`);
        break
    } else {
        document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${dice}</li>`);
    }
}
