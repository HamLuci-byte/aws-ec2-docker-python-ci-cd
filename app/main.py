from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def hello():
    #return "Hello Shawon! Python Flask is Running from AWS EC2 Docker.More tutorial:arsalan1234"
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
