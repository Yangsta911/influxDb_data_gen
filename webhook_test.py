from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello, CORS is enabled!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)