from falcon.request import TRUE_STRINGS


asd ={}
d = {"http://localhost:5200/":"polls"}

asd.__setitem__('http://localhost:5000/',"users")
asd.__setitem__('http://localhost:5100/',"posts")
asd.__setitem__('http://localhost:5101/',"posts")
asd.update(d)

for i in asd:
    print(i)

print(asd.items())

if "polls" in asd.values():
    print("True")
#print(asd)