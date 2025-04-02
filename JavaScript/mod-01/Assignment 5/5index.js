'use strict';
const year = parseInt(prompt('Type a year.'));

if (year) {
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                document.querySelector('#target').innerHTML = `${year} is a leap year.`
            } else {
                document.querySelector('#target').innerHTML = `${year} is not a leap year.`

            }
        } else {
            document.querySelector('#target').innerHTML = `${year} is a leap year.`
        }
    } else {
        document.querySelector('#target').innerHTML = `${year} is not a leap year.`
    }
} else {
    document.querySelector('#target').innerHTML = `Year not set.`
}