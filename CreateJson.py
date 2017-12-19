import json
from pathlib import Path
import os

class CreateJson ():
	"""docstring for CreateJson """
	def __init__(self, list : str[]):
		self.list = list
		

	def createDict(self):
		cwd = os.getcwd()
		data = {}
		for i in range(len(self.list):
			filename, file_extension = os.path.splitext(str(cwd+'/'+self.list[i]))
			if(file_extension == ".txt"):
				data[self.list[i]] = {"name": filename ,"extension": file_extension, "path" : str(cwd+'/'+filename), "type": "text"}

			else if (file_extension == ".png" or file_extension == ".jpg" or file_extension == "jpeg" or file_extension == ".gif"):
				data[self.list[i]] = {"name": filename ,"extension": file_extension, "path" : str(cwd+'/'+filename), "type": "picture"}

			else if (file_extension == ".mp4" or file_extension == ".mov" or file_extension == ".avi"):
				data[self.list[i]] = {"name": filename ,"extension": file_extension, "path" : str(cwd+'/'+filename), "type": "video"}

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