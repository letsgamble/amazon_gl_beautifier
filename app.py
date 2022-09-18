from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'many random bytes'

input_lists = []


@app.route('/')
def main():
    combined_list = list(dict.fromkeys(input_lists))
    replaced_list = [lst.replace('gl_', '') for lst in combined_list]
    _replaced_list = [lst.replace('_', ' ') for lst in replaced_list]
    return render_template('index.html', content=_replaced_list)


@app.route('/add_list/', methods=['GET', 'POST'])
def add_list():
    if request.method == 'POST':
        lst = request.form.get('gls')
        if len(list(lst)) > 0:
            input_lists.extend(list(lst.split(', ')))
            return redirect(url_for('main'))
