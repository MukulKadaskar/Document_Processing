from flask import Flask, render_template, request, redirect, url_for
from qrScanner import scanQR
from tesseractOCR import scanForText
from face_extractor import extract_face
from classify import classify
from forge import forge
from dbHandle import authenticateUser, isLoggedIn
import config

app = Flask(__name__, template_folder=config.TEMPLATE_FOLDER)


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form["login-username"]
        password = request.form["login-password"]
        if authenticateUser(username, password):
            print("Log in")
            return redirect(url_for('upload_file'))
        else:
            print("Fails")
            return redirect(url_for('login'))

# @app.route('/check', methods=['GET', 'POST'])
# def check_file():
#     if request.method == 'GET':
#         return render_template('check.html')
#     elif request.method == 'POST':
#         if request.form['class']:
#             res = classify('upload.png')
#             if res==1:
#                 return "Classifed as Aadhar."



@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        if isLoggedIn:
            return render_template('upload.html')
        else:
            return redirect(url_for('login'))
    elif request.method == 'POST':
        f = request.files['aadhar-card']
        # Getting Data from form: -  print(request.form["text"])
        f.save('uploads/upload.png')
        dataDict = scanQR('upload.png')
        result = classify('upload.png')
        if result==1:
            res='1.Classifed as Aadhar card.'
        else:
            res="1.Not classified as Aadhar card."
        extract_face('upload.jpg')
        prediction = forge('upload.png')
        if result == 1:
            pred = '2.Image is not tampered.'
        else:
            pred = '2.Image is tampered.'
        return render_template('response.html',
                               qrData=dataDict['PrintLetterBarcodeData'],
                               Image='output.jpg',
                               Image1='output.jpg',
                               OCR=scanForText(image="uploads/upload.png", preprocess="blur"),
                               result=res,
                               tamper=pred)
        # return render_template('check.html')


if __name__ == '__main__':
    app.run(debug=True)
