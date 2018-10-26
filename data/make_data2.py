import json

data = {
        "vol1": {"data":{"name": "volunteer1"}, "alloted": []}
        ,"vol2": {"data": {"name": "volunteer2"}, "alloted": []}
        ,"vol3": {"data": {"name": "volunteer3"}, "alloted": []}
    }

with open("volunteer.json", "w") as write_file:
    json.dump(data,write_file)
#print('\n')
