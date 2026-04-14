from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return ('''
    Wed design in this Triple quoted area
    <html> //title=home
    
    </html>
    ''')

@app.route("/about")
def about():
    return ('''
    Wed design in this Triple quoted area
    <html> //title=about 
    
    </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)
