from flask import Flask, render_template,request
from db_utils import main_page_db

app = Flask(__name__)

Total_Pages = 5



@app.route('/')
def main_page():
    page = request.args.get('page', 1, type=int)
    page = max(page, 1)
    offset = (page - 1) * Total_Pages
    data = main_page_db()
    return render_template('main_page.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)