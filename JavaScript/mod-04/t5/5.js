'use strict';

window.addEventListener("load", async () => {
    try {                                               // error handling: try/catch/finally
        const response = await fetch("https://api.chucknorris.io/jokes/random");    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        console.log(jsonData.value);    // log the result to the console
    } catch (error) {
        console.log(error.message);
    } finally {                                         // finally = this is executed anyway, whether the execution was successful or not
        console.log('asynchronous load complete');
    }
});