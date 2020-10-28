class User:
    def __init__(self,Username,Password):
        self.Username=Username
        self.Password=Password
        self.Progress=[0,0,0]
        self.Score=0

    def Calculate_Score(self):
        self.Score=sum(self.Progress)*10
