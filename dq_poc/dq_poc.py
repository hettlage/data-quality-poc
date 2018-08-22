from flask import Flask, render_template
from dq_poc.menus import primary_menu, primary_menu_item, secondary_menu, secondary_menu_item

app = Flask(__name__)


@app.route('/', defaults={'page': ''})
@app.route('/dq', defaults={'page': ''})
@app.route('/dq/<path:page>')
def hello(page):
    return render_template('index.html',
                           primary_menu=primary_menu(),
                           primary_menu_item=primary_menu_item(page),
                           secondary_menu=secondary_menu(page),
                           secondary_menu_item=secondary_menu_item(page))
