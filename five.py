#expert level python features
#4:40:00
'''
class cat:
    def __init__(self):
        self.meow()
#the above code runs although we haven't defined the method called meow()
# because unlike other programming language the python code is compiled at an execution time.
def makeClass(x):
    class Cat:
        def __init__(self,name):
            self.name = name

        def printV(self):
            print(x)
    return Cat

cls=makeClass(30)
pussy=cls("tony")
print(pussy.name)
pussy.printV()   

for x in range(10):#method inside the for loop
    def add():
        a=x+5
        print(a)

    add()    
#here if we call the add() outside the for loop then we will only get the last single calculated value 
def returnV(xy):
    if xy==5:
        print('The given value of x is equal to the 5')
    else:
        print('The given value of x is not equal to the 5')
    return returnV

#simple way to call the defined function is:   
returnV(50)
#another way is given below
#newReturn=returnV(59)
#newReturn()          
print(id(returnV))  #it actually gives the memory address id of the method


#expert2 
#magic method/__repr__()method
class person:
    def __init__ (self,name):
        self.name=name

    def __repr__(self):
        return f"person({self.name})"
    def __mul__(self,a):
        if type(a) is not int:
            raise Exception('invalid input,must be integer')
        self.name=self.name*a#multiplying the name by the int 'a'

    def __call__(self,b):
        print(b) 

    def __len__(self):
        return len(self.name)       
#after f in return part there should not be any space    
#in the above code we have to fetch the value of the object 'self.name'by writing inside the curly braces
# if we just call self.name then it will not fetch the value of the object but simply print self.name    
p=person('tim')
p*1# with mul
p(5)#with call,donot require print()
print(p)
print(len(p))


from queue import Queue
import inspect

q=Queue()#queue is a data strucure in python
print(q)
print(inspect.getsouce(Queue))
'''

#Meta classes
'''
def hello():
    class hi:
        pass

    return hi
hello()
#In python, classes are considered as an object unlike other programming language.
#classes create the objects and define the rules regarding how to create the objects 
#Similarly, meta classes create the classes and define the rules about creating the classes
class Test:
    pass
print(Test)
print(Test())
print(type(45))

def main():
    print('hello everyone')

print(type(main)) #gives the type of the function/method  
'''
class Test:
    pass

class Foe:
    def show(self):
        print('sewaro')

def add_attribute(self):
    self.p=667

Test=type('Test',(Foe,),{'a':45,'add_attribute':add_attribute })#without () in add_attribute
#in the above code class Foe is inherited in class Test ,while inheriting in this way we must leave a comma
# after writing the name of the parent class i.e. (classname,) 
#this line of code is equivalent to the code above, for creating the class Test from line 103 and 104
t=Test()
t.greet='Namaste
#we can define attribute outside of the class like regular classes
print(t.a)
print(t.greet)
print(t.show())
t.add_attribute()#first call with created object then print
print(t.p)

#we are going to create our own meta classes without using built in typw class,,,, created class inherits from type

#type inside the braces represent that meta class inherits from type 
class Meta(type):
    def __new__(self,class_name,bases,attrs):#__new__() method is called before the __init__()method, first thing always called when an object is created
          print(attrs)

          d={}#here a blank dictionary is created
          for name,value in attrs.items():
               if name.startswith("__"):#here if there is any name that starts with __ is simply stored inside value
                   d[name]=value
               else:#here names starting other than __ are converted into upper case
                   d[name.upper()]=value
          #print(d)           
          return type(class_name,bases,attrs)#these parameters are converted into upper case
    
class Cat(metaclass=Meta):
    a=8
    b=6
    def hi(self):
        print('hi')
#c=Cat() this line of code is optional 
c=Cat()
print(c.Hi())      
print("hello mangale")