#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
   return render_template('example.html')


@app.route('/map1')
def map1():
   return render_template('set_OSM_as_basemap.html')


@app.route('/map')
def map():
   return render_template('map.html')


if __name__ == '__main__':
   app.run()