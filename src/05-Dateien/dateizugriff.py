f = open("../../data/test.txt", "w")
f.write("Schreibe eine neue Datei\n")
f.write("und nochmals\n")
f.close()

f = open("../../data/test.txt","rt")
data = f.readlines();
f.close()
print(data[0],"XXX")
print(data[1])

print("Inhalt:")
for s in data:
    print(s,end="")

print("Inhalt:")
for s in data:
    print(s.rstrip())
    print("xx")
