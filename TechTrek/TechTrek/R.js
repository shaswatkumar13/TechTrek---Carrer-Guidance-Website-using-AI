document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('scan-button').addEventListener('click', function () {
        var resumeText = document.getElementById('resume-text').value;

        fetch('/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ resume_text: resumeText }),
        })
        .then(response => response.json())
        .then(data => {
            var resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            if (data.errors) {
                data.errors.forEach(function (error) {
                    resultDiv.innerHTML += `<p>${error}</p>`;
                });
            } else {
                resultDiv.innerHTML = '<p>No spelling mistakes found in the resume.</p>';
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
