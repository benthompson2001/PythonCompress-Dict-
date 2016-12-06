from collections import OrderedDict
import pickle
global k
k = 0
def part1():
    global k
    global finallist
    if k < now:
        finallist.append(ask[numbered[k]])
        k += 1
        part1()


print "Do you want to?: \n [1] Enter a string \n [2] Load a string"
welcome = raw_input("Please enter your choice: ")
if welcome == '1':
    ask = raw_input("Please enter a string: ")
    now = int(len(ask.split()))
    ask = ask.lower().split(" ")
    numbered = [ask.index(x) for x in ask]
    savename = raw_input("Please enter a file name for the data (eg. oliverreadabook): ")
    try:
        with open(savename + '.data', 'w') as openfile:
            pickle.dump([ask, numbered], openfile)
    except:
        with open(savename + '.data', 'wb') as openfile:
            pickle.dump([ask, numbered], openfile)
elif welcome == '2':
    global finallist
    finallist =[]
    filetoopen = raw_input("Please enter the filename for the data (eg. oliverreadabook): ")
    try:
        with open(filetoopen + '.data') as openfile:
            ask, numbered = pickle.load(openfile)
    except:
        with open(filetoopen + '.data', 'rb') as openfile:
            ask, numbered = pickle.load(openfile)
    ask = list(OrderedDict.fromkeys(ask))
    now = len(numbered)
    part1()
    finalstring = ' '.join(finallist)
    print ("Your string is: " + finalstring)
