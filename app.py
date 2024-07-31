from flask import Flask, render_template
from src.api.jokes import get_jokes

app = Flask(__name__)

@app.route('/')
def index():
    try:
        joke = get_jokes()
        return render_template('index.html', joke = joke)
    except Exception as e:
        return str(e)
    
if __name__ == "__main__":
    app.run(debug = True)