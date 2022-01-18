# Zahlen als Variable definieren und am Bildschirm ausgeben

x = 3
y = 5
z = x / y

# formatierte Ausgabe
print('z=' + "{:.2f}".format(z))

# oder
print('z=%.2f' % z)

# oder Standard-formatiert
print('z=%f' % z)

# oder unformatiert
print('z=', z)

# mehrer Werte ausgeben
print("%f/%f=%f" % (x, y, z))
print(x, '/', y, '=', z)

# besser lesbar
print("%(x).2f / %(y).2f = %(z).2f" % {
    'x': x,
    'y': y,
    'z': z
})
