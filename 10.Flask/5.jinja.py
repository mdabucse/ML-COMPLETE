# Building URL dynamically
# Variable Rule
# Jinja 2 Templete Engine


'''
{{}} -> Expressions to print output in the HTML
{% %} -> Conditions , for Loops
{# #} -> This is used for comment the line

'''

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

@app.route('/success/<score>') #Score vanthu Parameter antha parameter a nee link a kudukanum eg : http://127.0.0.1:5000/success/10
def success(score):
    res=''
    if int(score)>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html',results=res)
@app.route('/loop/<score>')  # For Looping in The HTML
def successloop(score):
    res=''
    if int(score)>=50:
        res='PASS'
    else:
        res='FAIL'
    exp = {'score':score,'res':res}
    return render_template('result1.html',results=exp)
@app.route('/ifcondition/<score>')  # For If conditions in The HTML
def successif(score):
    res=''
    if int(score)>=50:
        res='PASS'
    else:
        res='FAIL'
    exp = {'score':score,'res':res}
    return render_template('result.html',results=int(score))


if __name__ =='__main__':
    app.run(debug=True)