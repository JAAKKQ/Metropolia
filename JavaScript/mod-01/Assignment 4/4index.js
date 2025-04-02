'use strict';
const int1 = parseInt(prompt('Give integer one'));
const int2 = parseInt(prompt('Give integer two'));
const int3 = parseInt(prompt('Give integer three'));


document.querySelector('#target').innerHTML = `Sum of integers: ${int1+int2+int3}\nAvarage: ${(int1+int2+int3)/3}`