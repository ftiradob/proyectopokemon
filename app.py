import os
port=os.environ["PORT"]

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html")

app.run('0.0.0.0',int(port), debug=True)
