// Get the submit button
const submitButton = document.querySelector('#submit')

submitButton.addEventListener('click', function updateName (e) {
    e.preventDefault()
    // Get the name submitted by the user
    const name = document.querySelector('#name-input').value

    // Update the name on the page
    document.querySelector('#name-target').innerHTML = name
})
