# SmartQuiz App

## Introduction
The SmartQuiz App is an interactive application designed to provide quizzes on Python, JavaScript, and C++. It features real-time score tracking, user authentication, and a detailed score result page. This app aims to offer an engaging and educational tool for learners to test their knowledge in various programming languages.

## Features
- Real-time score tracking
- User authentication (login and registration)
- Detailed score result page showing percentage and correct/incorrect answers
- Responsive and user-friendly interface

## Technologies Used
- **Front-end**: HTML, CSS, JavaScript
- **Back-end**: Flask (Python)
- **Database**: JSON files for quiz questions, SQLite for user authentication

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gilfoye-CentriX/SmartQuiz_App.git
   cd SmartQuiz_App
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python3 -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the SQLite database**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   flask run
   ```

6. **Access the application**
   Open your browser and go to \http://127.0.0.1:5000/\

## Usage
- **Homepage**: Login or Create account
- **Dashboard**: Select a quiz category
- **Quiz**: Answer questions, with real-time score tracking
- **Score Result Page**: View percentage score and detailed results of correct/incorrect answers

## Future Improvements
- Expanding the question database
- Enhancing UI/UX
- Adding advanced user features like profile customization

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (\git checkout -b feature-branch\)
3. Commit your changes (\git commit -am 'Add new feature'\)
4. Push to the branch (\git push origin feature-branch\)
5. Create a new Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, feel free to reach out or create an issue on GitHub.

---

**GitHub Repository**: [SmartQuiz_App](https://github.com/Gilfoye-CentriX/SmartQuiz_App)
