# Der Datentype einer Variable ergibt sich nur durch die Initialisierung
# Es gibt in Python keine Deklaration einer Variablen

x = 5
print("Typ von x: ", type(x))
y = 3.0
print("Typ von y: ", type(y))
y = int(y)
print("Typ von y: ", type(y))

# VORSICHT Java-Programmierer: Division wird immer in float gerechnet 5/3 ergibt 1.6666, nicht 1 wie in Java
z = x / y
print("Typ von z: ", z)

# Strings
s = "Wort"
print("Typ von s: ", type(s), " Inhalt:", s)
s = 'worte ' * 5
print(s)
