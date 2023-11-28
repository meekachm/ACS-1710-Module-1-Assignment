# Import flask library
from flask import Flask
import random

# Create an instance of the flask server
app = Flask(__name__)

# Base route
@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

# Route to display a message based on the user's favorite animal
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

# Route to display a message based on the user's favorite dessert
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

# Route for a madlib story based on given adjectives and nouns
@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    return f'In a {adjective} world, there lived a {noun} who could {adjective}ly juggle marshmallows while singing opera!'

# Route to display the product of two numbers
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        result = int(number1) * int(number2)
        return f'{number1} times {number2} is {result}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

# Route to repeat a string a given number of times
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if n.isdigit() and int(n) > 0:
        return ' '.join([word] * int(n))
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

# Route to play a dice game
@app.route('/dicegame')
def play_dice():
    roll_result = random.randint(1, 6)
    if roll_result > 5:
        return f'You rolled a {roll_result}. You won!'
    return f'You rolled a {roll_result}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)
