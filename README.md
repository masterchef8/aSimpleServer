# aSimpleServer

A simple web server dedicated to respond to get method by sending a JSON file 
about files contained in the data folder. 
Three types of files are supported:
- Text files (.txt)
- Images (.png .jpg .jpeg .gif)
- Video (.mp4 .mov .avi)

{
"txt": {}, 
"img": 
    {
        "40-seignosse-aire-etape-camping-car-park-nouvelle-aquitaine.jpg": {
            "name": "40-seignosse-aire-etape-camping-car-park-nouvelle-aquitaine", 
            "extension": ".jpg", 
            "path": "data/40-seignosse-aire-etape-camping-car-park-nouvelle-aquitaine", 
            "type": "picture"}, 
        "maxresdefault.jpg": {
            "name": "maxresdefault", 
            "extension": ".jpg", 
            "path": "data/maxresdefault", 
            "type": "picture"}, 
        "plage.png": {
            "name": "plage", 
            "extension": ".png", 
            "path": "data/plage", 
            "type": "picture"}
        }, 
"video": {}
}