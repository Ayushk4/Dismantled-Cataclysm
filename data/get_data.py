import json

data_vic = {}
with open ("data/victim.json","r") as read_f:
    data_vic = json.load( read_f)

vic_ids = data_vic.keys()
data_array_vic = []

for keys in vic_ids:
    print(keys)
    data.append(data[keys])

#print(type(vic_ids))
#print(data_vic)
