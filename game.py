import requests
from flask import Flask, jsonify, render_template, request 
import  random 
# import 

app = Flask(__name__)

@app.route("/")

def home():
	return render_template('ui.html')
	
@app.route("/operation", methods=["POST"])
def operation():
    data = request.get_json()
    user_choice = data.get('choice', '').lower()
    
    choices = ['s', 'p', 'c']
    bot_choice = random.choice(choices)
    
    if user_choice == bot_choice:
        result = "draw"
    elif (user_choice == 's' and bot_choice == 'c') or \
         (user_choice == 'p' and bot_choice == 's') or \
         (user_choice == 'c' and bot_choice == 'p'):
        result = "win"
    else:
        result = "lose"
    
    return jsonify({
        'bot_choice': bot_choice,
        'result': result,
        'message': f"User choose: {user_choice}\nBot choose: {bot_choice}\nYou {'win!' if result == 'win' else 'lose!' if result == 'lose' else 'draw!'}"
    })

if __name__ == '__main__':
	app.run(debug=True)
