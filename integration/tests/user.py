# coding=utf-8
from tests import app

@app.route("/~user")
def url_with_tilde():
    return 'user'

@app.route("/!$&()*+,;=:@[]")
def url_weird():
    return 'weird'
