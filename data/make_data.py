import json

data = {
    "vic1" : {
        "data" : {"name" : "Nani", "location" : "IIT Kgp near MMM hall canteen", "ailment" : "broken leg"},
        "status" : "Unanswered",
        "alloted_to" : "None"
    },
    "vic2" : {
        "data" : {"name" : "Chinmoy", "location" : "Kharapur, near Dominoes", "ailment" : "Fell"},
        "status" : "Unanswered",
        "alloted_to" : "None"
    },
    "vic3" : {
        "data" : {"name" : "Apoorve", "location" : "Kharagpur city, near railway station", "ailment" : "lack of food supply"},
        "status" : "Unanswered",
        "alloted_to" : "None"
   }
}

with open("victim.json", "w") as write_file:
    json.dump(data,write_file)
#print('\n')