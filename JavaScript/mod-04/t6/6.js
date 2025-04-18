'use strict';

const form = document.getElementById("form")
const results = document.getElementById("results");


form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const query = document.querySelector('input[id=query]').value

    try {                                               // error handling: try/catch/finally
        const response = await fetch(`${form.action}?query=${query}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const shows = await response.json();          // retrieving the data retrieved from the response object using the json() function
        console.log(shows);    // log the result to the console

        results.innerHTML = ""
        for (const item of shows.result) {
            let article = document.createElement("article")
            article.classList.add("card")

            let desc = document.createElement("p")
            desc.innerHTML = item.value

            article.appendChild(desc)

            results.appendChild(article)
        }
    } catch (error) {
        console.log(error.message);
    } finally {                                         // finally = this is executed anyway, whether the execution was successful or not
        console.log('asynchronous load complete');
    }
})