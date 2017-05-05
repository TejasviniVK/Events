import json


class JsonHandler(object):
    def __init__(self):
        self.file = 'Data.json'


    def read_json(self):
        with open(self.file, 'r+') as f:
            if f.read() == '':
                f.seek(0)
                return
            else:
                f.seek(0)
                return json.load(f)


    def write_json(self, id,data):
        storage = self.read_json()
        with open(self.file, 'w+') as f:
            if not storage:
                storage={}
                storage.update({'cities':[data['Event_Place']],id:data})
                json.dump(storage, f, indent=4)
            else:
                if data['Event_Place'] not in storage['cities']:
                    storage['cities'].append(data['Event_Place'])
                storage.update({id:data})
                json.dump(storage, f, indent=4)
        return "Event Added Successfully!!"



    def delete_eventJH(self, del_ID):
        storage = self.read_json()
        if del_ID in storage:
            with open(self.file, 'w+') as f:
                del storage[del_ID]
                f.seek(0)
                json.dump(storage, f, indent=4)
                return "Successfull deletion."
        else:
            return "ID not found.Try Again"



    def update_eventJH(self, update_ID, dict1):
        storage = self.read_json()
        if update_ID in storage:
            with open("/Events/Data.json") as f:
                storage[id] = dict1
                if dict1['Event_Place'] not in storage['cities']:
                    storage['cities'].append(dict1['Event_Place'])
                json.dump(storage, f, indent=4)
                return "Successfully Updated."
        else:
            return "ID not found.Try Again."
