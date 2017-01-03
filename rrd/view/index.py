#-*- coding:utf-8 -*-
from flask import render_template
from rrd import app

@app.route("/dashboard")
def index():
    return render_template("index.html", **locals())
