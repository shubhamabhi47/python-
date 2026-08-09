# When we call a method of this object as myobject.method(arg1, arg2),
# this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) –
# this is all the special self is about.
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("Hello my name is " + self.name+" and I" +
              " work in "+self.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()
class GFG:
    def __init__(somename, name, company):
        somename.name = name
        somename.company = company

    def show(somename):
        print("Hello my name is " + somename.name +
              " and I work in "+somename.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()
