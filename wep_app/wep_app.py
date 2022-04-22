from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def page1():
    return render_template('page1.html')


@app.route('/chall1')
def chall1():
    return render_template('chall1.html')


@app.route('/chall2')
def chall2():
    return render_template('chall2.html')


@app.route('/award')
def award():
    return render_template('award.html')


@app.route('/chall1', methods=['POST', 'GET'])
def chall_1():
    term = False
    value = ''

    if request.method == 'POST' and request.form.get('value') == "720":
        term = True

    return render_template(
        "chall1.html",
        term=term
    )


@app.route('/chall2', methods=['POST', 'GET'])
def chall_2():
    term = False
    value = ''

    if request.method == 'POST' and request.form.get('value') == "астероид":
        term = True

    return render_template(
        "chall2.html",
        term=term
    )