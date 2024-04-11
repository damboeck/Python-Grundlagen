# Zahlen als Variable definieren und am Bildschirm ausgeben

x = 3
y = 5
z = x / y

# formatierte Ausgabe
print('z=' + "{:.2f} formatiert".format(z))

# oder
print('z=%.2f mit Platzhalter' % z)

# oder Standard-formatiert
print('z=%f einfach mit Platzhalter' % z)

# oder unformatiert
print('z=', z, " unformatiert")

# formatiert
print(f"z={z} formatiert")
print(f'z={z} formatiert')

# mehrer Werte ausgeben
print("%f/%f=%f" % (x, y, z))
print(x, '/', y, '=', z)

# besser lesbar
print("%(x).2f / %(y)f = %(z).2f" % {
    'x': 6.6,
    'y': y,
    'z': z
})

# einfaches Format
print(f"{x} / {y} = {z}")
