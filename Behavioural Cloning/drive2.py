from flask import Flask
app = Flask(__name__)

@app.route('/home')
def greet():
    return 'Hello srinath'
if __name__ == '__main__':
    app.run(debug=True)

