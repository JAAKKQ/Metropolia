'use strict';
const dices = parseInt(prompt("How many dices would you like to roll?"))
const sumEst = parseInt(prompt("What would you estimate the sum is?"))
let sum2 = 0

for (let i = 0; i <= 6**dices; i++) {
    let sum = 0
    for (let i = 0; i <= dices; i++) {
        sum += Math.floor(Math.random() * 6 + 1)
    }
    if (sum === sumEst) {
        sum2++
    }
}

document.querySelector('#target').innerHTML = `${6**dices/sum2}`
