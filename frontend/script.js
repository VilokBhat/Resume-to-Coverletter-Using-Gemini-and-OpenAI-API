document.getElementById('coverLetterForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const formData = new FormData();
    formData.append('resume', document.getElementById('resume').files[0]);
    formData.append('jobTitle', document.getElementById('jobTitle').value);
    formData.append('companyName', document.getElementById('companyName').value);

    try {
        const response = await fetch('http://localhost:5000/generate-cover-letter', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        document.getElementById('coverLetterOutput').value = result.coverLetter;  // Ensure the key matches the backend response
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to generate cover letter');
    }
});