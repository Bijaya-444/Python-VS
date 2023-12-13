#mutable and immutable type
#immutable types are those which canoot be changed after they have been defined
#such as:str,int,float,bool,bytes,tuple

#but mutable types are those which can be modified after they have been defined
#such as:list,dict,set

#explanation with code
'''a=(1,3)#tuple(immutable)
b=a
a=(4,5,6)
print(a,b)#output of b will be the unchanged/unmodified value of a, but output of a will be value after modification

#but the above case becomes different if we use mutable data types
x=[9,5]#list(mutable)
y=x
x=[5,6,7,8]
print(x,y)#here both the output of the x and y will be the value after modification


def get_largest_numbers(numbers,n):
    numbers.sort()

    return numbers[n:]
nums=[2,3,4,354,333,5,6]
print(nums)
largest=get_largest_numbers(nums,3)
print(nums)'''

#list comprehension
#simple example of comprehension
c=[ [j for j in range(5)] for i in range(5)]#for loop inside the list
print(c)
d=[a for a in range(10) if a%2==0]
print(d)

#function arguments and parameters types
def complicated_function(a,b,c):#up here a and b inside the braaces  are referred as parameters
    print(a,b)

complicated_function(2,b=33,c=456)#the order of passing the arguments must be according to the parameters orders
#we can pass the named arguments in any order but if we are going to pass the value of the unnamed parameters it must be in order
#here a and b inside the braces are referred as arguments    
#complication_function(b=33,2,c=456),this in incorrect because the declard order is a,b,c

def func(x,y,z=None):#N must be uppercase in None
    #if any parameters in the declard method is defined with None,then it is not necessary to pass the 
    #value of that argument
    print(x,y)

func(5,7,7)   

def f(a,b,*args):#*args, allows us to accept any numbers of positional arguments
    print(a,b,args)

f(3,5,586,6,66666,3)#value of the positional arguments(*args) must be passed after a and b

def ff(*args,**kwargs):# accept any numbers of keyword arguments
    print(args,kwargs['a'])#kwargs

ff(333,55433,a=5,e=6767,b=True,w='hell')#they are stored inside the dictionary and args are stored inside ()


#if__name__=="__main__": concept
def add(x,y):
    return x+y

if __name__== "__main__":
    print('running')

#Global Interpreter Lock(GIL)
#exclusive to python, any threads that wants to be executing needs to accquire interpreter lock.
# This means that we can only execute only one thread same time.
# each CPU have different numbers of core and each core can only execute one operation at a time.
# But inspite of having numbers of core, with GIL it will only execute one op at a time.


