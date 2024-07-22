from flask import Flask

app = Flask(__name__) # Creation of the Web server Gateway Interface


#Routing
@app.route('/') # Home Page
def welcome():
    return "Vanakkam Da Maapla Nalla Irukiya"

if __name__ =='__main__':
    app.run(debug=True)  # Run the App-> debug = True nu potom na Dynamic a Reload pannum Server each and every changes reflect in the Output Area