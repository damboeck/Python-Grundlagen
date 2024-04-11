'''
Created on 23.11.2011

@author: Werner
'''
def muster(x):
    print ('*'*(x+2))
    for i in range(x):
      print ('*' + ' '*x + '*')
    print ('*'*(x+2))

# ausprobieren:
muster(5)