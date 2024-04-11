from sympy import *

x,y,z,a,b,c,d,e,f,g,h,i,j,k,l=symbols("x,y,z,a,b,c,d,e,f,g,h,i,j,k,l")
g1=Eq(a*x+b*y+c*z,d)
g2=Eq(f*x+g*y+h*z,e)
g3=Eq(j*x+k*y+l*z,i)
L=solve([g1,g2,g3],[x,y,z])
print(L)