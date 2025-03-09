from flask import Flask, render_template

app = Flask(__name__)

# Home
@app.route('/')
def index():
    return render_template('index.html')
# Collections
@app.route('/collections')
def links():
    return render_template('collections.html')

# Profile
@app.route('/profile')
def scrapyard():
    return render_template('collections.html')

if __name__ == '__main__':
     app.run(debug=True)