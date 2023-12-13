import Third 
from Third import NotPrivate #this is the basic way of importing 

test =NotPrivate('tim')
#another way of importing third.py is [without writing second line and (test=Third.NotPrivate('tim'))]
test._display()