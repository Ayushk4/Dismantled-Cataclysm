import json

data = {
    "vic1" : {
        "data" : {"name" : "Nani", "location" : "IIT Kgp near MMM hall canteen", "ailment" : "broken leg"},
        "status" : 0,
        "alloted_to" : -1
    },
    "vic2" : {
        "data" : {"name" : "Chinmoy", "location" : "Kharapur, near Dominoes", "ailment" : "Fell"},
        "status" : 0,
        "alloted_to" : -1
    },
    "vic3" : {
        "data" : {"name" : "Apoorve", "location" : "Kharagpur city, near railway station", "ailment" : "lack of food supply"},
        "status" : 0,
        "alloted_to" : -1
    }
}

with open("victim.json", "w") as write_file:
    json.dump(data,write_file)
#print('\n')