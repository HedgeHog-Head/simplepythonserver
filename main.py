from flask import Flask

app = Flask(__name__)

@app.route('/')#what comes after backslash
def hello():
    return "this is a simple server, hello!"

@app.route('/version')
def version():
    return "This is version 1.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 9898) #local host and free port