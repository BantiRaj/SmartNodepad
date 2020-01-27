import NotePadModel
class Controller:
    def __init__(self):
        self.model=NotePadModel.Model()

    def save_file(self,msg,url):
        self.model.save_file(msg,url)

    def save_as(self,url,msg):
        self.model.save_as(url,msg)

    def read_file(self,url):
        self.result=self.read_file(url)
        return self.result

    def takeQuery(self):
        pass