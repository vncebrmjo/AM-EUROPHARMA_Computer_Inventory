from flask import Flask, render_template
from db_utils import main_page_db

app = Flask(__name__)

@app.route('/')
def main_page():
    data = main_page_db()
    return render_template('main_page.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)