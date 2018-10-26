from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename
import json
import os


UPLOAD_FOLDER = 'files_inputted/'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'ogg'])
#////////////// check for video file extention
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def get_data():
    data_vic = {}
    with open ("data/victim.json","r") as read_f:
        data_vic = json.load( read_f)

    vic_ids = data_vic.keys()
    data_array_vic = []

    for keys in vic_ids:
        data_vic[keys]["id"] = keys
        data_array_vic.append(data_vic[keys])

    return data_array_vic

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    data_array_vic = get_data()
    return render_template("home.html", data_array_vic = data_array_vic)

@app.route('/home', methods = ['POST'])
def homeSubmit():

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data_array_vic = get_data()
        return render_template("home.html", data_array_vic = data_array_vic)


    #    flash('Success')
    #    print("success")
    #print("\n\n\nasfsdgds\n\n")
    #new_data = request.form['victim_form']
    #print(new_data)
    else:
        data_array_vic = get_data()
        return render_template("home.html", data_array_vic = data_array_vic)

@app.errorhandler(404)
def pageNotFound(e):
    return ("Page Does Not Exist")

if __name__ == "__main__":
    app.run(debug=True)

#get_data()
