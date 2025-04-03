'use strict';

function roll() {
    return Math.floor(Math.random() * 6 + 1)
}

for (let i = 1; true; i++) {
    const dice = roll()
    if (dice === 6) {
        document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${dice}</li>`);
        break
    } else {
        document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${dice}</li>`);
    }
}

