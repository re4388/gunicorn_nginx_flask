from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Nginx as reverse Proxy to gunicorn"

# if __name__ == '__main__':
#     app.run(port=5001, debug=True)