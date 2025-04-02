'use strict';
const name = prompt('What is your name?');
const number = Math.floor(Math.random()*4)
console.log(number)
switch (number) {
    case 0:
        document.querySelector('#target').innerHTML = `${name} you are Gryffindor`
        break
    case 1:
        document.querySelector('#target').innerHTML = `${name} you are Slytherin`
        break
    case 2:
        document.querySelector('#target').innerHTML = `${name} you are Hufflepuff`
        break
    case 3:
        document.querySelector('#target').innerHTML = `${name} you are Ravenclaw`
        break

}