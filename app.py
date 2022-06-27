from flask import Flask, render_template, request, url_for
from datetime import datetime, date

azi = date.today()

app = Flask(__name__)
app.secret_key = "asecretkey"


@app.route('/', methods=['POST','GET'])
def home():

    name = request.form.get('name')
    if name != None:
        return render_template('bday.html', name=name, azi=azi)
    
    return render_template("home.html")

@app.route('/<name>', methods=['POST','GET'])
def bday(name):

    return render_template('bday.html', name=name, azi=azi)
    
    



def start_ngrok():
	#from flask_ngrok import run_with_ngrok#pip install flask-ngrok
    from pyngrok import ngrok
    url = ngrok.connect(5000)
    print('ngrok url = ', url)
#start_ngrok()


if __name__ == '__main__':
	app.run(debug=True)
