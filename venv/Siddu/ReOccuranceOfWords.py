file = "DataSet.txt"
sentance = open(file).read()

words = sentance.split()

x = dict()
repeated = []

for word in words:
    if word in x.keys():
        increase = (x.get(word)) + 1
        if(increase > 1 and word not in repeated):
            repeated.append(word)
        else:
            pass
        x.update({word:increase})
    else:
        x[word] = 1

print(repeated)
L = []
for word in repeated:
    y = x.get(word)
    z = str(y)+":"+word
    L.append(z)
    # print(word,x.get(word))

print(sorted(L))
