from flask import Flask, render_template
app = Flask(__name__)   

@app.route("/")
def home():
    return render_template("home.html")  //render home.html

@app.route("/about")
def about():
    return render_template("about.html")  //about.html render 

if __name__ == "__main__":
    app.run(debug=True)
