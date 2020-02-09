print("Hey this is Ritwick Joshi")

names=["ritwick","joshi","john","doe"]

listt = [[name] for name in names] #creating a 2d list

for name in listt:
  if len(name) == 1:
    print(name[0])