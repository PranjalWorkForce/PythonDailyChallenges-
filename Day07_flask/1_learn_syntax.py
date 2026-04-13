from flask import Flask, render_template_string

app = Flask(__name__)

# This is the "One File" approach using a Template String
# Note the {{ }} syntax used to display the variable
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Flask Page</title></head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>Math check (10 // 3): {{ 10 // 3 }}</p>
</body>
</html>
"""

@app.route('/')
def home():
    # Pass data into the template
    return render_template_string(HTML_TEMPLATE, name="Coder")

if __name__ == '__main__':
    app.run(debug=True)
