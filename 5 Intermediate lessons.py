#optional parameters
'''def add(x,y):#using optional parameters
    return x + y

print(add(6,8))
#using default parameters    
def square(a=9):
    return a **3

print(square() )
#another eg using op parameters

def add(name,address,freq=1):#here word is not optional,we have to provide its value in call
    #here freq parameters is made optional coz if no any value is given in the 
    #call it will simply take 1 as its value or take the given value in the call
    print((name+address)*freq)

call=add('votey ','ktm\n',5)

#eg
class car(object):
    def __init__(self,make,model,year,condition='new',kms=0):#cpndition and kms are optional
        self.make=make
        self.model=model
        self.year=year
        self.condition=condition
        self.kms=kms

    def display(self,showAll=False):
        if showAll:
            print('This car is %s %s from %s,and it is %s and has %s kms.' %(self.make,self.model,self.year,self.condition,self.kms))
        else:
            print('This car is a %s %s from %s.' %(self.make,self.model,self.year))

whip=car('ford','sniper ',2000)
whip.display(True)


#static and class methods

class student(object):
    Division = 'First division'
    
     #class variable
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    @classmethod
    def getDivision(cls):#here we used cls instead of self coz 'Division' is not an object
         #class method, in class method we dont require any object to access the class
        return cls.Division
       
    @staticmethod    
    def isAdult(age):#static method
        return age >=18
    def isMale(gender):
        return gender =='male' #bool

    def display (self):
        print('I am',self.name,' and I am ',self.age,'. My gender is ',self.gender)

tim=student('Tim',22,'male')
print(tim.display())
print(student.getDivision())#here we haven't declared any object but still we are able to aceess class var       
print(student.isAdult(13)) 
print(student.isMale('male'))       
# in static method paramters is optional(def ismale()/ismale(gender))  but in class method one 
# parameter is always compulsary (isMale(cls)) 


#Map function
li=[1,3,4,5,6]
def func(x):
    return x**x
#newLi=[]
#for x in li:
 #   newLi.append(func(x))

#print(newLi)  this above commented part is the simple way of printing the n^n of integers of the list 'li'   
#now the code  below displays the functionality of the map function with lesser code 
print(list(map(func,li))) 
#here map function is used which takes function 'func' and list 'li'
#as an arguments. And 'list' cannot be changed
print([func(x)for x in li])
print([func(x) for x in li if x%2==0])
#above two lines are without the map function , line comprehension


#Filter function
def add5(x):
    return x+5
def isOdd(x):
    return x%2!=0 #technically false and 0 are similar ,and 'hi','enkdkfj\', 1,True is similar 
def fact(y):
    return y*(y-1)
listy=[1,2,3,4,5,6]
print(list(filter(isOdd,listy)))
b= list(map(add5,listy))
c=list(map(add5,filter(isOdd,listy)))
print(c)
d=list(filter(isOdd,b))
e=list(map(isOdd,d))


#Lambda Function
def func(x):
    return x+5
print(func(5))

a=lambda y: y*5#lambda = anonymous function
print(a(6))
#using map function with the lambda function
a=[2,5,6,7,8,9]
b=list(map(lambda c:c*4,a))
print(b)
c=list(filter(lambda t:t%2==0,a))#lambda func with filter func
print(c)

#Introduction to Collections
#before using collections we have to import it 
#import collections
#from collections import Counter

#collections are built-in module in python,it allows us to have different data types so that we can store informations,very useful.
#Containers:containers in python is pretty much like a data type or an object which contains several items
#eg:- list,tuple,dictionary, set,etc.
#types
#counter,deque,namedTuple(),orderDict,defaultdict
'''
import collections
from collections import Counter
'''
c=Counter('gourmet')
print(c)
c=Counter([3,4,'hello',5,'sewaro'])#list
print(c)
print(c[5])
c=Counter({'b':1,'a':2})#dictionary
print(c)
c=Counter(cats=4,dogs=5)
print(c['dogs'])
print(list(c.elements()))

h=Counter (a=4,b=3,c=6,d=5)
o=Counter (a=4,b=3,c=6,d=5)
i=Counter(['a','b','b','c'])
h.subtract(i)
print(h)
h.update(i)
print(h)
h.clear()#clears the list
print(h)
x=h+i
print(x)
print(h-i)


#collections:named tuple
import collections
from collections import namedtuple
point=namedtuple('point','wx y z')#or either with list 
red=namedtuple('red',['a','b','c'])
newP=point(9,8,6)
newPP=red(33,44,55)
print(newP)#result:point(x=9,y=8,z=6)
print(newPP)
#and with dictionary 
green=namedtuple('green',{'wx':0,'b':0,'c':0})
newPPP=green(55,6,7)
print(newPPP)
#others simple ways of printing those created lists , tuples or dicts
print(newP.wx,newP.y,newP.z)
print(newP[0])
#we can also print the above the above created newPPP,presenting as the dictionary by using asdict()
print(newPPP._asdict())#newPPP._asdict()
print(newPPP._fields)
newPPP=newPPP._replace(wx=87787)#to replace the value of the tuples
print(newPPP)'''

#collections:deque(pronounced as dek)
import collections
from collections import deque
dek=deque('hallo')
dek.append('sewaro')
dek.appendleft('kirant')#adding element at the beginning of the list(deque)
dek.pop()#deletes the last element from the list by default 
dek.popleft()#deletes the first element from the list

#dek.clear()#clears the whole deque
dek.extend('45646')
#takes anything that is iterable:list,string,dict and put it at the end of the list
#deque and extend are quite similar coz after creating objects in list, every word of the string or 
#every numbers of the entered integer as a single object
#such thing don't happen while appending/adding
dek.extend([5,6,7,8])#extending list
dek.extendleft('soul')
#it will be added as 'l','o','u','s' coz extending on the left is done from s then u,o,l  at the beginning of the list
#the most useful method of the deque is rotate()
#it rotates the list left or right accordingly to the given positive or negative integer's value position
#if we give positive value in rotate then it will rotate the dek by that amount to the right side
#and if we give negative value in rotate it will rotate the dek by that amount to the left side
#positive dida pixadi ko agadi aauxa ra negative dida agadi ko pixadi janxa
dek.rotate(-2)


#print(dek)another useful property of the deque is 'maxlen',this property will limit the length of the list according to the given maxlen
#if we have set the maxlen to 4 and we already have four elements in the deque then if we add new elements
# then it will replace the elements from the beginning of the list and add from the end of the list.
d=deque('namaste',maxlen=5)
d.append('hi')
print(d) 