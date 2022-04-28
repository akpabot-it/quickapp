from flask import Flask
import crud

app = Flask(__name__)

with app.app_context():
    crud.get_articles()

if __name__ == '__main__':
    app.run(debug=True)
