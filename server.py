from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "password"

@app.route('/')
def gamepage():
    if 'thenumber' not in session:
        session['thenumber']= random.randint(1, 100)

    return render_template('index.html')

@app.route('/playing', methods=["POST"])
def playing():
    session["theguess"] = int(request.form['guess'])
    print(request.form)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True, port=5001)