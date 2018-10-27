from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename
import json
import os

from sampleSpacy import spacy_data

app = Flask(__name__)


def get_data():
    data_vic = {}

    with open ("data/victim.json","r") as r:
        data_vic = json.load(r)
    print(data_vic)
    vic_ids = data_vic.keys()
    data_array_vic = []

    for keys in vic_ids:
        data_vic[keys]["id"] = keys
        data_array_vic.append(data_vic[keys])

    f=open("data/volunteer.json", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    
    data_vol = {}
    with open ("data/volunteer.json","r") as read_f:    
        data_vol = json.load(read_f)

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



@app.route('/homeassign', methods = ['POST'])
def homeassign():
    
    data_array_vol, data_array_vic = get_data()

    vic_id_being_assigned = ""
    vol_code = ""
    for i in data_array_vic:
        try:
            vol_code = request.form[i["id"]]
            vic_id_being_assigned = i["id"]
        except:
            continue
        break

    print(vic_id_being_assigned)
    print("esdgsd")
   # print(vol_code)

    
    if vol_code != "" :
        for i in data_array_vol:
            if i["id"] == vol_code:
                i["alloted"].append(vic_id_being_assigned)
                new_vol = {}
                with open ("data/volunteer.json","r") as read_f:
                    new_vol = json.load( read_f)

                new_vol[i["id"]]["alloted"] = i["alloted"]
                
                with open ("data/volunteer.json","w") as wri:
                    json.dump(new_vol,wri)


                #vic_id_being_assigned = i["id"]

                new_vic = {}
                with open ("data/victim.json","r") as read_f:
                    new_vic = json.load( read_f)
                print(new_vic)
                print(new_vic[vic_id_being_assigned])
                
                new_vic[vic_id_being_assigned]["status"] = "Assigned to " + str(vol_code)
                new_vic[vic_id_being_assigned]["alloted_to"] = vol_code

                with open ("data/victim.json","w") as wri:
                    json.dump(new_vic,wri)

    data_array_vol, data_array_vic = get_data()
    return render_template("home.html", data_array_vic = data_array_vic, data_array_vol = data_array_vol)

@app.route('/homeSubmitVictim', methods = ['POST'])
def homeSubmitVictim():
    
    new_data = request.form['victim_form']
    #print("\n\n\nasfsdgds\n\n")
    #print(new_data)

    data_array_vol, data_array_vic = get_data()
    i = len(data_array_vic) +1
    name = []
    activity =[]
    donation =[]
    add = []
    number_of_people = []
    name, activity, donation, add, number_of_people= spacy_data(new_data)

    new_id = {}
    new_id["vic" + str(i)] = {}
    new_id["vic" + str(i)]["data"] = {}
    count =0
    if len(name) >0:
        new_id["vic" + str(i)]["data"]["name"] = name
        count+=1
    if len(activity) >0:
        new_id["vic" + str(i)]["data"]["ailment"] = activity
        count+=1
    if len(add) >0:
        strr='.'
        while strr in add:
            add.remove(strr)
        new_id["vic" + str(i)]["data"]["location"] = list(set(add))
        count+=1

    if len(number_of_people) >0:
        count+=1
        new_id["vic" + str(i)]["data"]["no of people"] = number_of_people
    
    if count == 0 :
        new_id["vic" + str(i)]["data"]["Undetected_text"] = new_data
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


@app.route('/homeSubmitVolunteer', methods = ['POST'])
def homeSubmitVolunteer():
    
    new_data = request.form['volunteer_form']
    #print("\n\n\nasfsdgds\n\n")
    print(new_data)

    data_array_vol, data_array_vic = get_data()
    i = len(data_array_vol) + 1

    name, activity, donation, add, number_people = spacy_data(new_data)

    new_id = {}
    new_id["vol" + str(i)] = {}
    new_id["vol" + str(i)]["data"] = {}

    count = 0
    if len(name) >0:
        count+=1
        new_id["vol" + str(i)]["data"]["name"] = name
    if len(donation) >0:
        count +=1
        new_id["vol" + str(i)]["data"]["donation"] = donation
    if len(add) >0:
        strr='.'
        while strr in add:
            add.remove(strr)
        if len(add) >0:
            new_id["vol" + str(i)]["data"]["location"] = list(set(add))
    if len(number_people) >0:
        count +=1
        new_id["vol" + str(i)]["data"]["number of people"] = number_people

    if count == 0 :
        new_id["vol" + str(i)]["data"]["Undetected_text"] = new_data

    new_id["vol" + str(i)]["alloted"] = []
    new_id["vol" + str(i)]["alloted_to"] = "None"


    data_vol = {}
    with open ("data/volunteer.json","r") as read_f:
        data_vol = json.load(read_f)
    data_vol["vol" + str(i)] = new_id["vol" + str(i)]
    with open("data/volunteer.json","w") as w:
        json.dump(data_vol,w)

    data_array_vol, data_array_vic = get_data()
    return render_template("home.html", data_array_vic = data_array_vic, data_array_vol = data_array_vol)



@app.errorhandler(404)
def pageNotFound(e):
    return ("Page Does Not Exist")

if __name__ == "__main__":
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
