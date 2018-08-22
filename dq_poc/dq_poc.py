from flask import Flask, render_template
from dq_poc.menus import primary_menu_item

app = Flask(__name__)


@app.route('/dq/<path:page>')
def hello(page):
    return render_template('index.html',
                           primary_menu_item=primary_menu_item(page))
