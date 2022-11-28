from flask import Flask 
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('empleados/index.html')

@app.route("/juan")
def juan():
    return render_template('empleados/juan.html')

if __name__ =='__main__':
    app.run(debug=True)