from main import rear as rear
from flask import Flask, request

app = Flask(__name__)
@app.route("/docClassifier", methods=['GET', 'POST'])
def main():
    return rear()


if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1',port=5000, threaded = False)
