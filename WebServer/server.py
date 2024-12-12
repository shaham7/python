from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_from():
    if request.method == 'POST':
        data = request.form.to.dict()
        print(data)
        return 'form submitted'
    return '??'