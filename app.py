from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "aaaaheloooooo asharf Hello Ashraf how are yod had dinner!"

app.run(host="0.0.0.0", port=5000)
