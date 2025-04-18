'use strict';

const form = document.getElementById("form")
const results = document.getElementById("results");


form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const query = document.querySelector('input[id=query]').value

    try {                                               // error handling: try/catch/finally
        const response = await fetch(`${form.action}?q=${query}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const shows = await response.json();          // retrieving the data retrieved from the response object using the json() function
        console.log(shows);    // log the result to the console

        results.innerHTML = ""
        for (const item of shows) {
            let article = document.createElement("article")
            article.classList.add("card")

            let heading = document.createElement("h2")
            heading.innerHTML = item.show.name

            let figure = document.createElement("figure")

            let image = document.createElement("img")
            if (item.show.image?.medium) {
                image.src = item.show.image?.medium
            } else {
                image.src = "https://upload.wikimedia.org/wikipedia/commons/a/a3/Image-not-found.png"
            }
            image.alt = item.show.name
            figure.appendChild(image)

            let link = document.createElement("a")
            link.target = "_blank"
            link.href = item.show.url
            link.innerHTML = item.show.url

            let desc = document.createElement("div")
            desc.innerHTML = item.show.summary

            article.appendChild(heading)
            article.appendChild(figure)
            article.appendChild(link)
            article.appendChild(desc)

            results.appendChild(article)
        }
    } catch (error) {
        console.log(error.message);
    } finally {                                         // finally = this is executed anyway, whether the execution was successful or not
        console.log('asynchronous load complete');
    }
})