from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename
import json
import os
from ir import spacy_data

app = Flask(__name__)


def get_data():
    data_vic = {}
    with open ("data/victim.json","r") as read_f:
        data_vic = json.load( read_f)

    vic_ids = data_vic.keys()
    data_array_vic = []

    for keys in vic_ids:
        data_vic[keys]["id"] = keys
        data_array_vic.append(data_vic[keys])

    data_vol = {}
    with open ("data/volunteer.json","r") as read_f:
        data_vol = json.load( read_f)

    vol_ids = data_vol.keys()
    data_array_vol = []

    for keys in vol_ids:
        data_vol[keys]["id"] = keys
        data_array_vol.append(data_vol[keys])

    return data_array_vol, data_array_vic


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    data_array_vol, data_array_vic = get_data()
    #print(len(data_array_vic))
    return render_template("home.html", data_array_vic = data_array_vic, data_array_vol = data_array_vol)

@app.route('/home', methods = ['POST'])
def homeSubmit():
    
    new_data = request.form['victim_form']
    print("\n\n\nasfsdgds\n\n")
    print(new_data)

    name, activity, donation, add = spacy_data(new_data)

    new_id = {}
    new_id["vic" + str(i)] = {}
    new_id["vic" + str(i)]["data"] = {}
    new_id["vic" + str(i)]["data"]["name"] = name
    new_id["vic" + str(i)]["data"]["ailment"] = activity
    new_id["vic" + str(i)]["data"]["location"] = add
    new_id["vic" + str(i)]["status"] = "Unanswered"
    new_id["vic" + str(i)]["alloted_to"] = "None"
    

    data_vic = {}
    with open ("data/victim.json","r") as read_f:
        data_vic = json.load(read_f)
    data_vic["vic" + str(i)] = new_id["vic" + str(i)]
    with open("data/victim.json","w") as w:
        json.dump(data_vic,w)

    data_array_vol, data_array_vic = get_data()
    return render_template("home.html", data_array_vic = data_array_vic, data_array_vol = data_array_vol)


@app.route('/homeassign', methods = ['POST'])
def homeassign():
    
    data_array_vol, data_array_vic = get_data()

    vic_id_being_assigned = ''
    for i in data_array_vic:
        try:
            vol_code = request.form[i["id"]]

        except:
            continue

        vic_id_being_assigned = i["id"]

        new_vic = {}
        with open ("data/victim.json","r") as read_f:
            new_vic = json.load( read_f)

        new_vic[vic_id_being_assigned]["status"] = "Assigned to " + vol_code
        new_vic[vic_id_being_assigned]["alloted_to"] = vol_code

        with open ("data/victim.json","w") as wri:
            json.dump(new_vic,wri)

        break

    if vol_code == "" :
        for i in data_array_vol:
            if i["ids"] == vol_code:
                i["alloted"].append()
                new_vol = {}
                with open ("data/volunteer.json","r") as read_f:
                    new_vol = json.load( read_f)

                new_vol[i["ids"]]["data"]["append"] = i["allotted"]
                
                with open ("data/volunteer.json","w") as wri:
                    json.dump(new_vol,wri)

    data_array_vol, data_array_vic = get_data()
    return render_template("home.html", data_array_vic = data_array_vic, data_array_vol = data_array_vol)



@app.errorhandler(404)
def pageNotFound(e):
    return ("Page Does Not Exist")

if __name__ == "__main__":
    i=4
    app.run(debug=True)




# string =
# UPLOAD_FOLDER = 'files_inputted/'
# ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'ogg'])
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#     return '.' in filename and \
#             filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS






# @app.route('/home', methods = ['POST'])
# def homeSubmit():

#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     # if user does not select file, browser also
#     # submit an empty part without filename
#     if file.filename == '':
#         flash('No selected file')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         data_array_vol, data_array_vic = get_data()
#         return render_template("home.html", data_array_vic = data_array_vic, data_array_vol = data_array_vol)


#     #    flash('Success')
#     #    print("success")
#     #print("\n\n\nasfsdgds\n\n")
#     #new_data = request.form['victim_form']
#     #print(new_data)
#     else:
#         data_array_vol, data_array_vic = get_data()
#         return render_template("home.html", data_array_vic = data_array_vic, data_array_vol = data_array_vol)





# @app.errorhandler(404)
# def pageNotFound(e):
#     return ("Page Does Not Exist")

# if __name__ == "__main__":
#     app.run(debug=True)

# #get_data()
