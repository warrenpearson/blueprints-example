from flask import Flask
from external.nomad import nomad

app = Flask(__name__)
app.register_blueprint(nomad)


@app.route("/")
def index():
    return "Hello World!"


# Start development web server
if __name__ == '__main__':
    app.run()
