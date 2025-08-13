from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    name="Roylkrishna"
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("index.html")

@app.route('/test')
def test():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("working.html")

@app.route('/cubic')
def sc():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("cubic.html")


@app.route('/plane')
def plane():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("plane.html")

@app.route('/cubic_plane')
def cubic_plane():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("cubic_plane.html")


@app.route('/test1')
def test1():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("test1.html")

@app.route('/cubic_test')
def cubic_test():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("cubic_test.html")


if __name__ == '__main__':
    app.run(debug=True)
