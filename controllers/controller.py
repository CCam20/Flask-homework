from app import app
from flask import render_template
from modules.order_list import *


@app.route("/")
def index():
    return render_template('index.html', orders = order_list)

@app.route("/order/<ordernum>")
def specific_order(ordernum):
    return render_template("order.html", order = order_list[int(ordernum)])
