document.addEventListener("DOMContentLoaded", function() {
    const score = localStorage.getItem('score');
    const totalQuestions = localStorage.getItem('totalQuestions');
    const correctAnswers = JSON.parse(localStorage.getItem('correctAnswers'));
    const incorrectAnswers = JSON.parse(localStorage.getItem('incorrectAnswers'));

    const percentageScore = (score / totalQuestions) * 100;

    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = `
        <p>Your score: ${score} out of ${totalQuestions} (${percentageScore.toFixed(2)}%)</p>
        <h2>Correct Answers:</h2>
        ${correctAnswers.map(question => `<p>${question.question} - Correct Answer: ${question.answer}</p>`).join('')}
        <h2>Incorrect Answers:</h2>
        ${incorrectAnswers.map(question => `<p>${question.question} - Correct Answer: ${question.answer}</p>`).join('')}
    `;
});
