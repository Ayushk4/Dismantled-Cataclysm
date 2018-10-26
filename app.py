from flask import Flask, render_template,request,url_for
import json
app = Flask(__name__)


def get_data():
    data_vic = {}
    with open ("data/victim.json","r") as read_f:
        data_vic = json.load( read_f)

    vic_ids = data_vic.keys()
    data_array_vic = []

    for keys in vic_ids:
    #    print(keys)
        data_vic[keys]["id"] = keys
        data_array_vic.append(data_vic[keys])

    #print(type(vic_ids))
    #print(data_array_vic)
    return data_array_vic


@app.route('/', methods=['GET','POST'])
def homePage():
    if request.method == 'POST':
        #CHECK FOR NULL DATA
        new_data = request.form.get('victim_form')
        print(new_data)

    data_array_vic = get_data()
    return render_template("home.html", data_array_vic = data_array_vic)

@app.errorhandler(404)
def pageNotFound(e):
    return ("Page Does Not Exist")

if __name__ == "__main__":
    app.run(debug=True)

#get_data()
