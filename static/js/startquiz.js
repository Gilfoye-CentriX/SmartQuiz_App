 function startQuiz(topic) {
    const urlMap = {
        'python': "{{ url_for('python_quiz') }}",
        'javascript': "{{ url_for('javascript_quiz') }}",
        'cpp': "{{ url_for('cpp_quiz') }}"
    };
    window.location.href = urlMap[topic];
}