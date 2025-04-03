'use strict';

const array = [
    "Johnny",
    "DeeDee",
    "Joey",
    "Marky"
]

function concat(array) {
    let string = ""
    for (let i = 0; i <= array.length-1; i++){
        string += array[i]
    }
    return string
}

document.querySelector('#target').innerHTML = concat(array);
