'use strict';
const number = parseInt(prompt("How many dices should I roll?"))

let sum = 0

for (let i = 0; i < number; i++) {
    const dice = Math.floor(Math.random()*6)+1
    sum += dice
    console.log(dice)
}

document.querySelector('#target').innerHTML = `${number} dices rolled with a total sum of ${sum}`