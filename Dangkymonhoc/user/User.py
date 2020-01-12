
class User():
    def __init__(self, usn, pw, q):
        self.usn = usn
        self.pw = pw 
        self.q = q
    
    def getUsn(self):
        return self.usn