from flask import Flask,render_template # render_template -> This module is used to redirect the HTML page

app = Flask(__name__)

@app.route('/')
def html():
    return "<h1>Hello</h1><br><h2>World</h2>"

@app.route('/index')
def html_file():
    return render_template('index.html')  #Importent Point -> Intha html file templetes nu oru folder kulla than irukanum illaina work aagathu 

if __name__ =='__main__':
    app.run(debug=True)