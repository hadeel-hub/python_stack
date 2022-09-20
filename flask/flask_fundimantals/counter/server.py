from itertools import count
from falsk import Flask, render_template
app = Flask(__name__)

@app.route("/count")
def counter():
    
    return render_template("index.html")