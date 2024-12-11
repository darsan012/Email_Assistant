// Handle tone selection buttons
const toneButtons = document.querySelectorAll('.tone-btn');

toneButtons.forEach(button => {
    button.addEventListener('click', () => {
        toneButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    });
});

// Handle form submission
const emailForm = document.getElementById('email-form');
const previewContent = document.querySelector('.preview-content');

emailForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const to = document.getElementById('to').value; // Recipient email
    const message = document.getElementById('message').value; // User's input
    const tone = document.querySelector('.tone-btn.active').textContent; // Selected tone

    try {
        const response = await fetch('/generate-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ to, message, tone }),
        });

        if (!response.ok) throw new Error("Failed to generate email");

        const emailData = await response.json();
        previewContent.innerHTML = `<pre>${emailData.email}</pre>`;
    } catch (error) {
        console.error("Error generating email:", error);
        previewContent.innerHTML = `<p>Error generating email. Please try again.</p>`;
    }
});
