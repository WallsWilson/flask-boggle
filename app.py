from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "SHHHHHHHHHHH SEEKRIT"

boggle_game = Boggle()

@app.route('/')
def boggle():
    board = boggle_game.make_board()
    session['board']=board
    return render_template('base.html', board=board)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form
    valid_word = boggle_game.check_valid_word(boggle(), data)
    return jsonify(data, valid_word,)
    