from flask import Flask, render_template, request, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'many random bytes'


@app.route('/', methods=['GET', 'POST'])
def main():
    if session.get("list") is None:
        session["list"] = []
    if request.method == 'POST':
        session['gls'] = request.form.get('gls')
        session["list"].extend(list(session['gls'].split(', ')))
        combined_list = list(dict.fromkeys(session["list"]))
        replaced_list = [lst.replace('gl_', '') for lst in combined_list]
        _replaced_list = [lst.replace('_', ' ') for lst in replaced_list]
        return render_template('index.html', content=_replaced_list)
    return render_template('index.html')


@app.route('/delete/')
def delete():
    session["list"] = []
    session.clear()
    return redirect(url_for('main'))
