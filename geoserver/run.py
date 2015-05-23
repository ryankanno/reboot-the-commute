# -*- coding: utf-8 -*-

import os
from eve import Eve
from flask import render_template

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

app = Eve(template_folder=tmpl_dir, static_folder=static_dir)

@app.route("/nearby/<string:latitude>/<string:longitude>")
def nearby_map(latitude, longitude):
    return render_template('nearby.html', latitude=float(latitude),
            longitude=float(longitude))

if __name__ == '__main__':
    app.run(host=host, port=port)
