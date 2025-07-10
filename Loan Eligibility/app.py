from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DUMMY_USER = 'anjali@gmail.com'
DUMMY_PASS = '12345678'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email == DUMMY_USER and password == DUMMY_PASS:
        return redirect('/loan')
    else:
        return render_template('login.html', error="Invalid credentials")

@app.route('/loan', methods=['GET', 'POST'])
def loan_form():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        grad = request.form['grad']
        job = request.form['job']
        salary = int(request.form['salary'])
        dep = int(request.form['dep'])
        cb = int(request.form['cb'])
        loan1 = int(request.form['loan1'])

        eligible = age > 18 and grad == 'yes' and job == 'yes' and 575 <= cb <= 900
        loan2 = 0

        if eligible:
            base_amt = (10 / 100) * salary
            ded = (0.05) * dep * base_amt
            loan2 = int(base_amt - ded)

        return render_template('result.html', eligible=eligible, name=name, age=age, loan2=loan2)

    return render_template('loan_form.html')

if __name__ == '__main__':
    app.run(debug=True)
