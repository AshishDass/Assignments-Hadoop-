import string
file=open("example.txt","r")
d1=dict()
for line in file:
    line=line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ") 
    for word in words: 
        if word in d1: 
            d1[word] = d1[word] + 1
        else: 
            d1[word] = 1
for key in d1:
    print(key,":",d1[key])
  