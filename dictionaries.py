thisDic = {
    "A": "Audrey",
    "B" : "Bacana",
    "C" : "Charmosa"
}

print(thisDic)

for key in thisDic:
    print(key + ": " + thisDic[key])

for i in thisDic.items():
    print(i)

for i in thisDic.keys():
    print(i)