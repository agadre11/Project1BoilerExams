from flask import Flask, render_template
import requests

app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def home():

    #url = "https://api.boilerexams.com/questions/1f86e0a7-0736-4f45-85d7-b0e4cdf5f969"
    #url = "https://api.boilerexams.com/questions/425ef734-29f3-4b4f-9f1e-5c3617849e47"
    #math_string = r"A line $l$ passes through the points $A(1,-2,1)$ and $B(2,3,-1)$. At what point does this line intersect with the $x y$-plane?"
    
    response = requests.get(url)
    print(response.json())
    '''data = response.json()
    qType = data['type']
    math_string = data['data']['body']
    options = []
    if qType == 'MULTIPLE_CHOICE':
        for i in data['data']['answerChoices']:
            options.append(i['body'])
        question_data = {
        "text": math_string,
        "options": options,
        "correct_index": data['data']['solution'][0]
        }
        print(question_data)
    else:
        question_data = {
        "text": math_string,
        "answer": data['data']['solution']
        }
        print(question_data)'''

    '''question_data = {
        "text": r"A line $l$ passes through $A(1,-2,1)$ and $B(2,3,-1)$. At what point does it intersect the $xy$-plane?",
        "options": [
            r"$(2, 3, 0)$",
            r"$(\frac{3}{2}, \frac{1}{2}, 0)$",  # Correct answer
            r"$(0, 0, 0)$",
            r"$(1, -2, 0)$",
            r"None of the above" # 5th option example
        ],
        "correct_index": 1  # 0-based index (so 1 is the second option)
    }'''
    '''if qType == 'MULTIPLE_CHOICE':
        return render_template('multipleChoice.html', q=question_data)
    else:
        return render_template('freeResponse.html', q=question_data)'''

if __name__ == '__main__':
    app.run(debug=True)