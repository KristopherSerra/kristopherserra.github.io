from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Facil")
def facil():
    return render_template("Facil.html")

@app.route("/Medio")
def medio():
    return render_template("Medio.html")

@app.route("/Dificil")
def dificil():
    return render_template("Dificil.html")

@app.route("/Dificultad")
def Main():
    return render_template("Dificultad.html")

if __name__ == "__main__":
    app.run(debug=True, port=2024)

