from pathlib import Path


class CreateListofFile():
    """docstring for JsonUtils"""

    def __init__(self, path: str):
        self.path = path
        self.list = list(Path(path).glob('*,*'))
        self.convertListToString()

    def convertListToString(self):
        for i in range(len(self.list)):
            self.list[i] = self.list[i].name

    def getList(self) -> str:
        return str(self.list)
