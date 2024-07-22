from flask import Flask,render_template, request

app = Flask(__name__)



@app.route('/index',methods=['GET'])
def html_file():
    return render_template('index.html')  

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method =='POST':
        name = request.form['name'] # name -> id in the HTML page
        return f'Hello {name}'
    return render_template('form.html')


if __name__ =='__main__':
    app.run(debug=True)