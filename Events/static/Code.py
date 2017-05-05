
def write_Json(data,ID):
    file='Data.json'
    os.stat(file)
    with open(file,'w+') as f:
        storage={}
        storage[ID]=data
        json.dump(data,f,indent=4)
        return "Event Added Successfully!!"