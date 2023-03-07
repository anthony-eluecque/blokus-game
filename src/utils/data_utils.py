import json
import os
import datetime

class jsonManager():

    @staticmethod
    def writeJson(data:dict,outfile = './src/models/data.json')->None:
        with open(outfile,"w") as file:
            file.write(json.dumps(data,indent=4))
        file.close()

    @staticmethod
    def readJson(file = './src/models/data.json')->dict:
        with open(file,"r") as outfile:
            data = json.load(outfile)
        outfile.close()
        return data

class dataGame():

    def __init__(self) -> None:
        
        if os.path.exists('./src/models/data.json'):
            self.data = jsonManager.readJson()
        else:
            date = datetime.datetime.now()
            heure = str(date.hour) + "h" + str(date.minute)
            date = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
            self.data = jsonManager.readJson()
            self.data["parties"]["1"]["heure"] = heure
            self.data["parties"]["1"]["date"] = date
            jsonManager.writeJson(self.data)



