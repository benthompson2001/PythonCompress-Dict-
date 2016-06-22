
ask = input("Please enter a sentence \n: ")
ask = ask.lower()
ask = ask.split()
numbered = [ask.index(x)+1 for x in ask]
print(ask, numbered)
