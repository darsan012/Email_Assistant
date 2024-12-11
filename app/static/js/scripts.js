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

emailForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const to = document.getElementById('to').value;
    const message = document.getElementById('message').value;
    const tone = document.querySelector('.tone-btn.active').textContent;

    previewContent.innerHTML = `
        <p><strong>Subject:</strong> Generated Reply</p>
        <p>Dear ${to || 'Recipient'},</p>
        <p>${message}</p>
        <p>Best regards,</p>
        <p>CreatAI Team</p>
    `;
});