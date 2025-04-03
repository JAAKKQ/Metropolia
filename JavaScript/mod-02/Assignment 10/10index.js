'use strict';

const positions = parseInt(prompt("How many candidates would like to have in this vote?"))

let candidates = []

for (let i = 1; i <= positions; i++) {
    const candidate_name = prompt(`What is the name of candidate ${i}/${positions}?`)
    candidates.push({
        name: candidate_name,
        votes: 0,
    })
}

const voters = parseInt(prompt("How many voters are there?"))

for (let i = 1; i <= voters; i++) {
    const voted = prompt(`Who would you like to vote ${i}/${voters}?`)
    if (voted) {
        const person = candidates.find(p => p.name === voted)
        if (person) {
            person.votes += 1
        }

    }
}

candidates.sort((a, b) => b.votes - a.votes)

console.log(`The winner is ${candidates.at(0).name} with ${candidates.at(0).votes} votes.`)
for (let i = 0; i <= candidates.length-1; i++) {
    console.log(`${candidates[i].name}: ${candidates[i].votes} votes`)
}