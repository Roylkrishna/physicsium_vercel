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



@app.route('/tetragonal')
def tetragonal():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("tetragonal.html")



@app.route('/hexagonal')
def hexagonal():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("hexagonal.html")


@app.route('/orthorhombic')
def orthorhombic():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("orthorhombic.html")

@app.route('/monoclinic')
def monoclinic():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("monoclinic.html")

@app.route('/triclinic')
def triclinic():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("triclinic.html")

@app.route('/trigonal') 
def trigonal():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("trigonal.html")


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


@app.route('/draw_with_parameters')
def plotly():
    #return render_template("AtomicSolid-Vpython.html")
    return render_template("plotly.html")


if __name__ == '__main__':
    app.run(debug=True)
