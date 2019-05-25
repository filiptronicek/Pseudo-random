import random
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
iterations = 0
desIterations = 10000
for x in range(desIterations):
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
    print("Ones: " + str(one)+" | twos: "+str(two) + " | threes: "+str(three) +
          " | fours: "+str(four)+" | fives: "+str(five)+" | sixes: "+str(six) + " | iterations: " + str(iterations))
print("%: Ones: " + str(round((one / iterations)*100, 2)) + "%  Twos: " + str(round((two /
                                                                                     iterations)*100, 2)) + "% Threes: " + str(round((three / iterations)*100, 2))+"% Fours: " + str(round((four / iterations)*100, 2))+"% Fives: " + str(round((five / iterations)*100, 2))+"% Sixes: " + str(round((six / iterations)*100, 2))+"%")
input()
