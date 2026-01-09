from flask import Flask, render_template
import requests

app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def home():

    url = "https://api.boilerexams.com/questions/1f86e0a7-0736-4f45-85d7-b0e4cdf5f969"
    #math_string = r"A line $l$ passes through the points $A(1,-2,1)$ and $B(2,3,-1)$. At what point does this line intersect with the $x y$-plane?"
    
    response = requests.get(url)
    data = response.json()
    math_string = data['data']['body']
    return render_template('index.html', formula=math_string)

if __name__ == '__main__':
    app.run(debug=True)