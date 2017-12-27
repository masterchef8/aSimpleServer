import json
import os


class CreateJson:
    """docstring for CreateJson """

    def __init__(self, path=os.getcwd()):
        self.path = path
        if self.path == os.getcwd():

            self.path = os.getcwd()+'/data'
            self.list = os.listdir(self.path)
        else:
            self.list = os.listdir(self.path)

    @property
    def createDict(self):

        data = {}
        for i in range(len(self.list)):
            filename, file_extension = os.path.splitext(str(self.path + '/' + self.list[i]))
            if data == {}:
                data['txt'] = {}
                data['img'] = {}
                data['video'] = {}

            if file_extension == ".txt":

                data['txt'][self.list[i]] = {"name": filename, "extension": file_extension,
                                      "path": str(self.path + '/' + filename), "type": "text"}

            elif file_extension == ".png" or file_extension == ".jpg" or file_extension == "jpeg" or \
                    file_extension == ".gif":

                data['img'][self.list[i]] = {"name": filename, "extension": file_extension,
                                      "path": str(self.path + '/' + filename), "type": "picture"}

            elif file_extension == ".mp4" or file_extension == ".mov" or file_extension == ".avi":
                data['video'][self.list[i]] = {"name": filename, "extension": file_extension,
                                      "path": str(self.path + '/' + filename), "type": "video"}

        json_file = json.dumps(data)
        print(json_file)
        return json_file


"""
JSON{
	http://developer.rhino3d.com/guides/rhinopython/python-dictionary-database/
	datastore = { "office": {
    "medical": [
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }
    ],
    "parking": {
      "location": "premium",
      "style": "covered",
      "price": 750
    }
  }
}
}
"""
