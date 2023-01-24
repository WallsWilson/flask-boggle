const form = document.getElementById('submitForm')
form.addEventListener('submit', async (e) => {
    e.preventDefault()
    try{
        const response = await axios.post('/submit', {data: form.elements})
        console.log(response)
    } catch(error) {
        console.log(error)
    }
})

function score() {
    const guess = document.getElementById('guess');
    const startingScore = "0"
    let score = guess.length;
    if(guess == valid_word) {
        newScore = startingScore + score;
           newScore.innerHTML = "score"
    }
}