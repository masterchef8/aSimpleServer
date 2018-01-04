import json
import os

class CreateJson:
    """docstring for CreateJson """

    def __init__(self, path=os.getcwd(), net_adress="193.50.110.74:8888"):
        self.path = os.getcwd() + '/data'
        self.net_address = net_adress
        self.list = os.listdir(self.path)
        self.net_address_data = "http://"+net_adress+"/"+"data"

        self.createDict()
    def createDict(self):

        data = {}
        for i in range(len(self.list)):
            filename, file_extension = os.path.splitext(str(self.path + '/' + self.list[i]))
            if data == {}:
                data['txt'] = {}
                data['img'] = {}
                data['video'] = {}

            if file_extension == ".txt":

                data['txt'][self.list[i]] = {"name": self.list[i], "extension": file_extension,
                                             "path": str(self.net_address_data + '/' + self.list[i]), "type": "text"}

            elif file_extension == ".png" or file_extension == ".jpg" or file_extension == "jpeg" or \
                    file_extension == ".gif":

                data['img'][self.list[i]] = {"name": self.list[i], "extension": file_extension,
                                             "path": str(self.net_address_data + '/' + self.list[i]), "type": "picture"}

            elif file_extension == ".mp4" or file_extension == ".mov" or file_extension == ".avi":
                data['video'][self.list[i]] = {"name": self.list[i], "extension": file_extension,
                                               "path": str(self.net_address_data + '/' + self.list[i]), "type": "video"}

        json_file = json.dumps(data)
        print(json_file)
        obj = open('data.txt', 'wb+')
        j = json_file.encode()
        obj.write(j)
        obj.close()
        # return json_file

