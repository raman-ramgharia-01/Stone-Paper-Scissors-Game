Stone Paper Scissors Game

A modern web-based implementation of the classic Stone Paper Scissors game, built with Python Flask backend, AJAX for seamless gameplay, and a responsive frontend.


🎮 Features

Interactive Gameplay: Play against the computer in real-time

Dynamic UI: Modern interface with weapon descriptions and visual feedback

AJAX Integration: Smooth gameplay without page reloads

Score Tracking: Real-time win/loss/draw statistics

Responsive Design: Works on both desktop and mobile devices


🛠️ Technologies Used
Backend: Python Flask

Frontend: HTML, CSS, JavaScript

Communication: AJAX (Fetch API)

Game Logic: Pure Python


📋 Game Rules
Stone beats Scissors (crushes them)

Scissors beat Paper (cuts them)

Paper beats Stone (wraps it)


🚀 Installation & Setup

Clone the repository

bash
git clone https://github.com/your-username/stone-paper-scissors.git
cd stone-paper-scissors
Create a virtual environment (optional but recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install flask
Run the application

bash
python app.py
Open your browser and navigate to

text
http://localhost:5000


📁 Project Structure

text
stone-paper-scissors/
│
├── app.py              # Main Flask application
├── static/
│   ├── css/           # Stylesheets
│   ├── js/            # JavaScript files
│   └── images/        # Game assets
├── templates/
│   └── index.html     # Main game interface
├── requirements.txt   # Python dependencies
└── README.md         # This file


🎯 How to Play

Select your weapon (Stone, Paper, or Scissors)

Click "Play Game" to challenge the computer

View the results and see who won

Track your score in the statistics section

Use "Reset Game" to clear scores and start fresh


🔧 Key Functions

Backend (Flask)

play_game(): Handles game logic and computer choice generation

determine_winner(): Compares player and computer choices

Score tracking and session management

Frontend (JavaScript/AJAX)

playGame(): Sends player choice to server via AJAX

updateUI(): Dynamically updates game results and scores

resetGame(): Resets the game state and statistics


🎨 UI Components

Weapon Selection: Three interactive cards for Stone, Paper, Scissors

Game Results Panel: Shows player choice, result, and computer choice

Statistics Counter: Tracks wins, draws, and losses

Control Buttons: Play Game and Reset Game functionality


🔄 AJAX Implementation

The game uses AJAX calls to:

Send player's weapon choice to the server

Receive game results without page refresh

Update scores and game state in real-time


🐛 Troubleshooting
Common Issues:

Flask not found: Run pip install flask

Port already in use: Change port in app.py

AJAX not working: Check browser console for errors


🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request


📄 License

This project is licensed under the MIT License - see the LICENSE file for details.


👏 Acknowledgments

Classic Stone Paper Scissors game

Flask documentation and community

All contributors and testers

Enjoy the game! May your stone always crush the scissors! ✊📄✂️