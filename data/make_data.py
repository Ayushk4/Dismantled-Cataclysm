import json

data = {
    "vic1" : {
        "data" : {"name" : "vic1_name"},
        "status" : 0,
        "alloted_to" : -1
    },
    "vic2" : {
        "data" : {"name" : "vic2_name"},
        "status" : 0,
        "alloted_to" : -1
    },
    "vic3" : {
        "data" : {"name" : "vic3_name"},
        "status" : 0,
        "alloted_to" : -1
    }
}

with open("victim.json", "w") as write_file:
    json.dump(data,write_file)
#print('\n')