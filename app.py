import random
import sys


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
iterations = 0
desIterations = 1000000

print("Calculating " + str(desIterations) + " random numbers")

for x in progressbar(range(desIterations), "",40):
    randNum = random.randint(1, 6)
    if randNum == 1:
        one += 1
    elif randNum == 2:
        two += 1
    elif randNum == 3:
        three += 1
    elif randNum == 4:
        four += 1
    elif randNum == 5:
        five += 1
    elif randNum == 6:
        six += 1
    iterations += 1

		
		

print("1: " + str(round((one / iterations)*100, 2)) + "%  \n2: " + str(round((two /                           iterations)*100, 2))+"% \n3: " + str(round((three / iterations)*100, 2))+"% \n4: " + str(round((four / iterations)*100, 2))+"% \n5: " + str(round((five / iterations)*100, 2))+"% \n6: " + str(round((six / iterations)*100, 2))+"%")
input()
