from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('./about.html')

@app.route('/<string:page_name>')
def works(page_name):
	return render_template(page_name)