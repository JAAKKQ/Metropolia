'use strict';
const answer = confirm("Should I calculate the square root?")
console.log(answer)
if (answer) {
    const number = parseFloat(prompt("Give me a number."))
    if (number >= 0) {
        document.querySelector('#target').innerHTML = `The square root of ${number} is ${Math.sqrt(number)}`
    } else {
        document.querySelector('#target').innerHTML = `The square root of a negative number is not defined`

    }
} else {
    document.querySelector('#target').innerHTML = `The square root is not calculated.`
}