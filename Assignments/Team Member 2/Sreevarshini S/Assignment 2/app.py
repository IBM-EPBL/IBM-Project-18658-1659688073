from flask import Flask, flash
from flask import render_template,request
app = Flask(__name__)
@app.route("/")
def signin():
    return render_template("signin.html")

@app.route("/home/",methods=('GET','POST'))
def home():
    if request.method=='POST':
        password=request.form['pass'] 
        if not password:
            flash('Password is required')
    return render_template("home.html")

@app.route("/signup.html/")
def signup():
    return render_template("signup.html")

@app.route("/about.html/")
def about():
    return render_template("about.html")
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
