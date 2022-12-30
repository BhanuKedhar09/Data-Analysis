import os
import json
from urllib.request import urlretrieve


def download_data():
    
    local_fname = 'border-crossing.json'
    url = "http://faculty.cs.niu.edu/~dakoop/cs503-2022fa/a3/border-crossing.json"
    if not os.path.exists(local_fname):
        urlretrieve(url, local_fname)
    return local_fname

def get_data():
    local_fname = download_data()
    data = json.load(open(local_fname));
    return data
    


def parse_data():
    data = get_data()
    temp = dict()
    temp[data[0]["Port Code"]] = {"name" : data[0]["Port Name"], "border" : data[0]["Border"], "state": data[0]["State"],
                                  "monthly_data" : {data[0]["Date"] : {data[0]["Measure"] : data[0]["Value"]}}}
    for d in data:
        t = (d["Port Code"],d["Date"])
        if t[0] not in temp.keys():
            k = {"name" : d["Port Name"], "border" : d["Border"], "state": d["State"],
                          "monthly_data" : {d["Date"] : {d["Measure"] : d["Value"]}}}
            temp[t[0]] = k
        else:
            if t[1] not in temp[t[0]]["monthly_data"].keys():
                temp[t[0]]["monthly_data"][t[1]] = {d["Measure"] : d["Value"]}
            else :
                temp[t[0]]["monthly_data"][t[1]].update({d["Measure"] : d["Value"]})
                    
    return temp
            
        
        
    
    

# temp = parse_data()

# print(temp[3425])



#ignore below
#3402: {'name': 'Noyes', 'border': 'Canada', 'state': 'Minnesota', 'monthly_data': {'Nov 2010': {'Train Passengers': 0}}}