const input1 = document.getElementById("num1")
const input2 = document.getElementById("num2")

const operation = document.getElementById("operation")
const trigger = document.getElementById("start")

const resultParagraph = document.getElementById('result');

trigger.addEventListener('click', () => {
    const num1 = parseFloat(input1.value)
    const num2 = parseFloat(input2.value)
    const oper = operation.value

    let result
    switch(oper) {
        case "add":
            result = num1 + num2
            break
        case "sub":
            result = num1 - num2
            break
        case "multi":
            result = num1 * num2
            break
        case "div":
            result = num1 / num2
            break
    }

    resultParagraph.textContent = `The result is: ${result}`
})