document.addEventListener('DOMContentLoaded', () => {
    const chatbox = document.getElementById('chatbox');
    const chatbotForm = document.getElementById('chatbot-form');
    const userInput = document.getElementById('user-input');

    chatbox.innerHTML = `<p><strong>SugarSage:</strong> Welcome! Ask me anything about diabetes or related information.</p>`;

    // Prediction functionality
    document.getElementById('predict-button').addEventListener('click', () => {
        const form = document.getElementById('prediction-form');
        const resultSection = document.getElementById('prediction-result-section');
        const heartMask = document.getElementById('heart-mask');
        const predictionPercentage = document.getElementById('prediction-percentage');

        // Validate required fields
        const inputs = form.querySelectorAll('input[required], select[required]');
        let isValid = true;
        let missingFields = [];

        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                missingFields.push(input.name);
            }
        });

        if (!isValid) {
            alert('Please fill in all required fields. Missing: ' + missingFields.join(', '));
            return;
        }

        // Get the form data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        // Convert values to appropriate types
        data.gender = parseFloat(data.gender);
        data.age = parseFloat(data.age);
        data.hypertension = parseFloat(data.hypertension);
        data.heart_disease = parseFloat(data.heart_disease);
        data.smoking_history = parseFloat(data.smoking_history);
        data.bmi = parseFloat(data.bmi);
        data.HbA1c_level = parseFloat(data.HbA1c_level);
        data.blood_glucose_level = parseFloat(data.blood_glucose_level);

        fetch('https://sugarsageapi-6bdf53d39be8.herokuapp.com/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Server error: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (!data.probability) {
                    throw new Error('Missing probability in response');
                }

                // Display the prediction percentage
                const probability = parseFloat(data.probability.trim().replace('%', ''));
                predictionPercentage.innerText = `Probability: ${Math.round(probability)}%`;
                heartMask.style.height = `${probability}%`;

                // Trigger animation effects
                setTimeout(() => {
                    heartMask.classList.add('show-mask', 'animate-heart');
                }, 50);

                // Show result section
                resultSection.classList.remove('hidden', 'opacity-0');
                resultSection.classList.add('show', 'opacity-100');
                form.classList.add('hidden');
            })
            .catch(error => {
                chatbox.innerHTML += `<p><strong>Error:</strong> ${error.message}</p>`;
                console.error('Error occurred:', error.message);
                form.classList.remove('hidden');
                resultSection.classList.remove('show');
                resultSection.classList.add('hidden');
                alert('An error occurred while predicting. Please try again.');
            });
    });

    // Fill Another Form functionality
    document.getElementById('fill-another-form').addEventListener('click', () => {
        const resultSection = document.getElementById('prediction-result-section');
        const form = document.getElementById('prediction-form');

        // Reset form and UI
        resultSection.classList.add('hidden', 'opacity-0');
        resultSection.classList.remove('show', 'opacity-100');
        form.classList.remove('hidden');
        form.reset();
        const heartMask = document.getElementById('heart-mask');
        heartMask.style.height = '0';
        heartMask.classList.remove('show-mask', 'animate-heart');
    });

    // Chatbot functionality
    chatbotForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent page reload on form submission

        const message = userInput.value.trim();
        if (!message) return; // Do nothing if input is empty

        // Append user message to chatbox
        chatbox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
        userInput.value = ''; // Clear input field

        // Send message to server
        fetch('https://sugarsageapi-6bdf53d39be8.herokuapp.com//chatbot', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: message }),
        })
            .then(response => response.json())
            .then(data => {
                // Append server response
                chatbox.innerHTML += `<p><strong>SugarSage:</strong> ${data.response}</p>`;
                chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll to the bottom

                if (message.toLowerCase() === "end") {
                    collectFeedback();
                }
            })
            .catch(error => {
                console.error('Error:', error);
                chatbox.innerHTML += `<p><strong>Error:</strong> Unable to get a response from the server.</p>`;
                chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll to the bottom
            });
    });

    // Feedback collection for sentiment analysis
    function collectFeedback() {
        const feedback = prompt("Please provide your feedback:");
        if (feedback) {
            fetch('/sentiment', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ feedback }),
            })
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                })
                .catch(error => console.error('Error:', error));
        }
    }

    // Smooth scroll for navigation buttons
    document.getElementById('go-to-chatbot').addEventListener('click', () => {
        document.getElementById('chatbot-section').scrollIntoView({
            behavior: 'smooth'
        });
    });
});
