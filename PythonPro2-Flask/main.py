from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect("PythonPro2-Flask/quiz.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quiz')
    data = cursor.fetchall()
    quiz_text = ''
    for quiz in data:
        quiz_text += f"<input type='radio' name='quiz_type' value='{quiz[0]}'>{quiz[0]}. {quiz[1]} <br>"
    return f"""
<h1 style="text-align:center;">Kuis</h1>
<form action="/test" method="get" style="text-align:center;">
    {quiz_text}
    <button type="submit">Mulai Kuis</button>
</form>
"""

@app.route('/test')
def test():
    conn = sqlite3.connect("PythonPro2-Flask/quiz.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM question')
    data = cursor.fetchall()
    quiz_text = ''
    for quiz in data:
        quiz_text += f"<h2>{quiz[0]}. {quiz[1]}</h2> <br>"
        quiz_text += f"""
        <div>
        <input type='radio' name='{quiz[0]}' value="{quiz[2]}">{quiz[2]}
        <input type='radio' name='{quiz[0]}' value="{quiz[3]}">{quiz[3]}
        <input type='radio' name='{quiz[0]}' value="{quiz[4]}">{quiz[4]}  
        <input type='radio' name='{quiz[0]}' value="{quiz[5]}">{quiz[5]}
        </div>
        <br>    
        """

    return f"""
<h1 style="text-align:center;">Kuis</h1>
<form action="/result" method="post" style="text-align:center;">
    {quiz_text}
    <a href="/">Kembali ke halaman awal</a>
    <button type="submit">Submit</button>
</form>
"""

@app.route('/result', methods=['POST'])
def result():
    conn = sqlite3.connect("PythonPro2-Flask/quiz.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM question')
    data = cursor.fetchall()
    data_form = request.form.to_dict()
    correct_answer = 0
    wrong_answer = 0
    for quiz in data:
        if quiz[2] == data_form.get(str(quiz[0])):
            correct_answer += 1
        else:
            wrong_answer += 1
    
    return f"""
<h1 style="text-align:center;">Result</h1>
<h1 style="text-align:center;">JAWABAN BENAR: {correct_answer}</h1> <br>
<h1 style="text-align:center;">JAWABAN SALAH: {wrong_answer}</h1> <br>
<a href="/">Kembali ke halaman awal</a>

"""

if __name__ == "__main__":
    # Starting the web server:
    app.run()