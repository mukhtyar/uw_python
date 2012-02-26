"""
Minimal Flask + forms demo

Send HTML page that echoes message from HTTP request
To get started, point browser at echo_flask.html
"""

from flask import Flask, render_template, request
import bookdb

# form_page is now a template

# No need for message page
# Flask converts view function return string to HTML page

app = Flask(__name__)

app.debug = True # development only - remove on production machines

# View functions generate HTTP responses including HTML pages and headers

@app.route('/books.html')
def form():
    return render_template('index.html', book_titles=titles)

@app.route('/get_detail.py')
def detail_page():
    # Flask Quickstart suggests request.form should work, but here it is empty
    # Flask converts return string to HTML page
    bookid = request.args['id']
    info = books.title_info(bookid)
    return render_template('detail.html', book_info=info)

# No function needed for other routes - Flask will send 404 page

if __name__ == '__main__':
    books = bookdb.BookDB()
    titles = books.titles()
    app.run()

