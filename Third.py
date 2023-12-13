'''class Nation(object):
    def __init__(self,name,nationality):
        self.name = name
        self.nationality = nationality
    def speak(self):
        print('Hi I am',self.name,'and my nationality is ',self.nationality)

ram=Nation('Rakesh','Indian') 
ram.speak()   
class State(Nation):
    def __init__(self,name,nationality,stateName):
        super().__init__(name,nationality)
        self.stateName = stateName
    def introduce(self):
        print('I am from',self.stateName)
shyam=State('hari','Russian','Ukraine')
shyam.introduce()  

#example of class inheritance
class Education(object):
    def __init__(self,name,age,level):
        self.name = name
        self.age = age
        self.level = level
    def speak(self):
        print('Hi I am',self.name,'and my age is ',self.age,'and my education level is ',self.level)

class Organization(Education):
    def __init__(self,name,age,level,orgName):
        super(). __init__(name,age,level)
        self.orgName = orgName
        
    def speak(self):
        print('Hi I am',self.name,'and my age is ',self.age,'and my education level is ',self.level)
    def Name(self):
        print('And the name of my educational oraganization is', self.orgName)

fande=Education('Fande',25,'bachelor',)
fande.speak()
votey=Organization('Votey',23,'bachelor','ASCOl')
votey.speak()
votey.Name()            
'''
#public and private classes
class _Private:
    #if uderscore '_' is used before any class name then it is considered as private class
    def __init__(self,name):
        self.name=name

class NotPrivate:
    #here no underscore is used so the defined class is public
    def __init__(self,name):
        self.name=name
        self.priv=_Private(name)
    def _display(self): #private method 
        print('Namaste')
    def display2(self):
        print('Sewaro')        
      


