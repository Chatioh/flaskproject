document.querySelector('form').onsubmit = async function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(this); // Get the form data
    if (!formData.get('file')) {
        alert("Please select a file to upload.");
        return;
    }

    const response = await fetch('/', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const result = await response.text(); // Get the response as text
        const resultDiv = document.querySelector('.result');
        if (resultDiv) {
            resultDiv.innerHTML = result; // Display result
        }
    } else {
        console.error('Error:', response.statusText);
        const resultDiv = document.querySelector('.result');
        if (resultDiv) {
            resultDiv.innerHTML = 'Failed to classify image.';
        }
    }
};