'use strict';
const start = parseInt(prompt("Give start year."))
const end = parseInt(prompt("Give end year."))

function isLeapYear(year) {
    if (year) {
        if (year % 4 === 0) {
            if (year % 100 === 0) {
                if (year % 400 === 0) {
                    return true
                } else {
                    return false
                }
            } else {
                return true
            }
        } else {
            return false
        }
    } else {
        return false
    }
}

let list = []

for (let year = start; year <= end; year++) {
    if (isLeapYear(year)) {
        document.querySelector('#target').insertAdjacentHTML('beforeend', `<li>${year}</li>`);
    }
}
