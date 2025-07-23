from flask import Flask, render_template, request #,redirect, flash
from main import getPrediction
#Save images to the 'static' folder as Flask serves images from this directory
UPLOAD_FOLDER = 'static/images/'
import numpy as np
import pandas as pd

#Create an app object using the Flask class. 
app = Flask(__name__, static_folder="static")
app.debug=False 

# routes


@app.route('/')
@app.route('/first')
def first():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/working')
def working():
    return render_template('working.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')  

@app.route('/login')
def login():
    return render_template('login.html')  



@app.route('/chart')
def chart():
    return render_template('chart.html') 



@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')

        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df) 




@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
	return render_template("index1.html")


@app.route("/notebook")
def notebook():
	return render_template("notebook.html")



@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = UPLOAD_FOLDER + img.filename	
		img.save(img_path)

		p = getPrediction(img_path)
		if p == 0:
			result = "Benign"
		elif p == 1:
			result= "Early Pre-B"
		elif p ==2:
			result= "Pre-B"
		else: 
			result= "Pro-B"



	return render_template("index_report.html", prediction = result, img_path = img_path)

if __name__ == "__main__":
    app.run()

