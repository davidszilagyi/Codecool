import sys

class Program():
    def __init__(self):
        self.name = "World"
    def NameCheck(self):
        if(len(sys.argv) > 1):
            self.name = sys.argv[1]
    def PrintIt(self):
        print("Hello " + str(self.name) + "!")

app1 = Program()
app1.NameCheck()
app1.PrintIt()