from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question')
def get_question():
    question_id = request.args.get('id')
    if not question_id:
        flash("Please enter a Question ID.", "error")
        return redirect(url_for('home'))

    url = f"https://api.boilerexams.com/questions/{question_id}"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            flash(f"Error fetching question. Status Code: {response.status_code}", "error")
            return redirect(url_for('home'))
            
        data = response.json()
        
        # Check if the response contains the expected data structure
        if 'data' not in data or 'type' not in data:
             flash("Invalid question data received from API.", "error")
             return redirect(url_for('home'))

        qType = data['type']
        math_string = data['data']['body']
        
        if qType == 'MULTIPLE_CHOICE':
            options = []
            for i in data['data']['answerChoices']:
                options.append(i['body'])
            question_data = {
                "text": math_string,
                "options": options,
                "correct_index": data['data']['solution'][0]
            }
            return render_template('multipleChoice.html', q=question_data)
        else:
            question_data = {
                "text": math_string,
                "answer": data['data']['solution']
            }
            return render_template('freeResponse.html', q=question_data)

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)