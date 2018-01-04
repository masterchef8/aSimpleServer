# aSimpleServer

A simple web server dedicated to respond to get method by sending a JSON file 
about files contained in the data folder. 
Three types of files are supported:
- Text files (.txt)
- Images (.png .jpg .jpeg .gif)
- Video (.mp4 .mov .avi)

{"txt": {}, "img": {"40-seignosse-aire-etape-camping-car-park-nouvelle-aquitaine.jpg": {"name": "40-seignosse-aire-etape-camping-car-park-nouvelle-aquitaine.jpg", "extension": ".jpg", "path": "/Users/somebody/git/aSimpleServer/data//Users/somebody/git/aSimpleServer/data/40-seignosse-aire-etape-camping-car-park-nouvelle-aquitaine", "type": "picture"}, "maxresdefault.jpg": {"name": "maxresdefault.jpg", "extension": ".jpg", "path": "/Users/somebody/git/aSimpleServer/data//Users/somebody/git/aSimpleServer/data/maxresdefault", "type": "picture"}, "plage.png": {"name": "plage.png", "extension": ".png", "path": "/Users/somebody/git/aSimpleServer/data//Users/somebody/git/aSimpleServer/data/plage", "type": "picture"}}, "video": {}}
