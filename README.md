# SmartQuiz App

SmartQuiz App is an interactive web application designed to provide quizzes on various programming languages including Python, JavaScript, and C++. This app helps users test and improve their coding knowledge.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- Quizzes for Python, JavaScript, and C++
- Interactive user interface
- Real-time score tracking
- User-friendly design

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Gilfoye-CentriX/SmartQuiz_App.git
    cd SmartQuiz_App
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Choose a quiz and start testing your knowledge!

## Project Structure
- `app.py`: Main application script.
- `static/`: Contains static files (CSS, JavaScript).
- `templates/`: Contains HTML templates.
- `cpp_questions.json`: C++ quiz questions.
- `javascript_questions.json`: JavaScript quiz questions.
- `python_questions.json`: Python quiz questions.

## Contributing

Contributions are welcome! Please fork this repository and create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to all contributors and open-source libraries used in this project.
