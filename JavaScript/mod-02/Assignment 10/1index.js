'use strict';
const number = parseInt(prompt("Give me a number."))

if (number <= 1) {
    document.querySelector('#target').innerHTML = `${number} is not a prime number :(`
} else {
    let isPrime = true;
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        document.querySelector('#target').innerHTML = `${number} is a prime number!`
    } else {
        document.querySelector('#target').innerHTML = `${number} is not a prime number :(`
    }
}

