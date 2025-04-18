'use strict';

const form = document.getElementById("form")

form.addEventListener('submit', async (event) => {
    //event.preventDefault();
    const query = document.querySelector('input[id=query]').value

    try {                                               // error handling: try/catch/finally
        const response = await fetch(`${form.action}?q=${query}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        console.log(jsonData);    // log the result to the console
    } catch (error) {
        console.log(error.message);
    } finally {                                         // finally = this is executed anyway, whether the execution was successful or not
        console.log('asynchronous load complete');
    }
})