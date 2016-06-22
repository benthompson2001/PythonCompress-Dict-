ask = input("Please enter a sentence \n: ")
ask = ask.lower().split(" ")
numbered = [ask.index(x)+1 for x in ask]
print(ask, numbered)
print("copyright oliver and blek schuut")
