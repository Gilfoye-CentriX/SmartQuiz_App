document.addEventListener("DOMContentLoaded", function() {
    let questions = [];
    let currentQuestion = 0;
    let score = 0;
    const totalQuestions = 10;
    const timeLimit = 90; // 1 minute 30 seconds
    let timer;

    fetch('/api/javascript_questions')
    .then(response => response.json())
    .then(data => {
        questions = shuffleArray(data).slice(0, totalQuestions);
        showQuestion(currentQuestion);
        updateButtonVisibility();
        startTimer(timeLimit);
    })
    .catch(error => {
        console.error("Error fetching questions: ", error);
    });

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    function showQuestion(index) {
        const question = questions[index];
        const questionContainer = document.getElementById("question-container");
        questionContainer.innerHTML = `<div class="question-card"><h2 class="question-text">${question.question}</h2></div>`;
        question.options.forEach(option => {
            questionContainer.innerHTML += `
            <div class="option-container" onclick="selectOption('${option}', '${question.answer}')">
                ${option}
            </div>`;
        });
    }

    window.selectOption = function(selected, correct) {
        if (selected === correct) {
            score++;
        }
        if (currentQuestion < questions.length - 1) {
            currentQuestion++;
            showQuestion(currentQuestion);
        } else {
            showScore();
        }
        updateButtonVisibility();
    };

    window.prevQuestion = function() {
        if (currentQuestion > 0) {
            currentQuestion--;
            showQuestion(currentQuestion);
        }
        updateButtonVisibility();
    };

    window.nextQuestion = function() {
        if (currentQuestion < questions.length - 1) {
            currentQuestion++;
            showQuestion(currentQuestion);
        }
        updateButtonVisibility();
    };

    function updateButtonVisibility() {
        document.getElementById('prev-button').style.display = currentQuestion > 0 ? 'inline' : 'none';
        document.getElementById('next-button').style.display = currentQuestion < questions.length - 1 ? 'inline' : 'none';
        document.getElementById('submit-button').style.display = currentQuestion === questions.length - 1 ? 'inline' : 'none';
    }

    function startTimer(seconds) {
        let remainingTime = seconds;
        const timerElement = document.createElement('div');
        timerElement.id = 'timer';
        document.body.insertBefore(timerElement, document.body.firstChild);

        timer = setInterval(() => {
            if (remainingTime > 0) {
                remainingTime--;
                timerElement.textContent = `Time Remaining: ${Math.floor(remainingTime / 60)}:${remainingTime % 60 < 10 ? '0' : ''}${remainingTime % 60}`;
            } else {
                clearInterval(timer);
                showScore();
            }
        }, 1000);
    }

    window.showScore = function() {
        clearInterval(timer);
        const scoreMessage = `Quiz completed! Your score is ${score} out of ${questions.length}.`;
        if (confirm(scoreMessage)) {
            window.location.href = '/';
        }
    };
});
