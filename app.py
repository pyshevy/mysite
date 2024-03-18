from flask import Flask, url_for, render_template

app = Flask(__name__)

# url_for('static', filename='style.css')

@app.get("/<name>")
def hello_world(name):
    return render_template('base.html')

if __name__ == '__main__':
    app.run(
        debug=True
    )