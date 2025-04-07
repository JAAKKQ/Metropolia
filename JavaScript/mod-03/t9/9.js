const inputField = document.getElementById("calculation")
const trigger = document.getElementById("start")
const resultParagraph = document.getElementById('result');

trigger.addEventListener('click', () => {
    const input = inputField.value.trim();

    let operand1, operand2, operator, result;

    if (input.includes('+')) {
        [operand1, operand2] = input.split('+');
        operator = '+';
        result = parseInt(operand1) + parseInt(operand2)
    } else if (input.includes('-')) {
        [operand1, operand2] = input.split('-');
        operator = '-';
        result = parseInt(operand1) - parseInt(operand2)
    } else if (input.includes('*')) {
        [operand1, operand2] = input.split('*');
        operator = '*';
        result = parseInt(operand1) * parseInt(operand2)
    } else if (input.includes('/')) {
        [operand1, operand2] = input.split('/');
        operator = '/';
        result = parseInt(operand1) / parseInt(operand2)
    }

    resultParagraph.textContent = `The result is: ${result}`
})