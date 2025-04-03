'use strict';

const array = [
    2,
    7,
    4
]

function even(array) {
    let evens = []
    for (let num of array) {
        if (num % 2 === 0) {
            evens.push(num)
        }
    }
    console.log("Original:", array)
    console.log("New Array:", evens)
    return evens
}

document.querySelector('#target').innerHTML = even(array);
