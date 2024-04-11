# numerisch differenzieren und integrieren
import scipy.integrate as integral

def f(x):
    return x**2
A=integral.quad(f,0,5)
print("Flächeninhalt A=",A[0])
print("A=",A)
print("F=",5*5*5/3)