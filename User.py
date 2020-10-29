class User:
    def __init__(self,Username,Password):
        self.Username=Username
        self.Password=Password
        self.Progress=set()
        self.Score=0

    def __str__(self):
        s=self.Username+'\n'+str(self.Progress)+'\n'+str(self.Score)
        return s
