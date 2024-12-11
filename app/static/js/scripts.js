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

emailForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent page reload

    // Get form values
    const to = document.getElementById('to').value;
    const message = document.getElementById('message').value;
    const tone = document.querySelector('.tone-btn.active').textContent;

    // Simulate email generation
    alert(`Email generated for ${to} with tone: ${tone}`);
});