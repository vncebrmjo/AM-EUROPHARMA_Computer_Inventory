from flask import Flask, render_template, request
from db_utils import main_page_db, main_page_limit

app = Flask(__name__)





@app.route('/')
def main_page():
    table = main_page_db()
    page_limit = main_page_limit()

    return render_template('main_page.html', table=table, page_limit=page_limit)


if __name__ == "__main__":
    app.run(debug=True)