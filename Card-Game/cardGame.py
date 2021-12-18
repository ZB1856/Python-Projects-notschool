import random
deck = []
playerhand = []
robothand = []
won, lost = 0, 0
sList = ["", ""]
def safeIntInput(message, min, max):
    loopvar = False
    while not loopvar:
        try:
            userinput = int(input(message))
            if not min == None:
                if userinput >= min:
                    if not max == None:
                        if userinput <= max:
                            loopvar = True
                            return userinput
                        else:
                            print("That number is too high my guy. ")
                    else:
                        loopvar = True
                        return userinput
                else:
                    print("That number is too low, bro. ")
            else:
                if not max == None:
                    if userinput <= max:
                        loopvar = True
                        return userinput
                else:
                    loopvar = True
                    return userinput
            

        except ValueError as ex:
            print("That's not an acceptable value, broski.")
    return userinput
#Dictionary of which cards kill other cards
killDict = {
    "Fire": "Snow",
    "Snow": "Water",
    "Water": "Fire"
}

def drawcards():
    global deck
    global playerhand
    global robothand
    temp = random.randint(1, len(deck)-1)
    playerhand.append(deck[temp])
    deck.remove(deck[temp])
    temp2 = random.randint(1, len(deck)-1)
    robothand.append(deck[temp2])
    deck.remove(deck[temp2])

#Generating cards here. Easier than making a massive list of dictionaries by hand
def myfunc():
    global deck
    global suit
    for x in range(1,11):
        deck.append({
            "suit": suit,
            "number": x        
    })
def createDeck():
    global suit, deck, playerhand, robothand
    print("Clearing deck / hands")
    deck.clear()
    playerhand.clear()
    robothand.clear()
    print("Creating deck now")
    for suit in ["Fire", "Snow", "Water"]:
        myfunc()
    for x in range(3):
        drawcards()

def choosecard():
    global playerhand
    global robothand
    print("Choose a card to play: ")
    print("1: " + str(playerhand[0]["suit"]) + " " + str(playerhand[0]["number"]))
    print("2: " + str(playerhand[1]["suit"]) + " " + str(playerhand[1]["number"]))
    print("3: " + str(playerhand[2]["suit"]) + " " + str(playerhand[2]["number"]))
    global playerchoice
    global robotchoice
    playerchoice = playerhand[safeIntInput("", 1, 3)-1]
    robotchoice = random.choice(robothand)

def comparecards(playercard, robotcard):
    global wonTurn
    print("You played " + str(playercard["suit"]) + " " + str(playercard["number"]))
    print("The robot played " + str(robotcard["suit"]) + " " + str(robotcard["number"]))
    if killDict[playercard["suit"]] == robotcard["suit"]:
        wonTurn = True
    elif killDict[robotcard["suit"]] == playercard["suit"]:
        wonTurn = False
    else:
        if playercard["number"] > robotcard["number"]:
            wonTurn = True
        else:
            wonTurn = False
def gameloop():
    global deck
    global won, lost
    global playerhand
    global robothand
    if len(deck) > 2:
        choosecard()
        comparecards(playerchoice, robotchoice)
        playerhand.remove(playerchoice)
        if wonTurn == True:
            print("You won!")
            won += 1 
        else:
            print("You lost.")
            lost += 1 
        wlindex = [won, lost]
        for thing in wlindex:
            if thing != 1:
                sList[wlindex.index(thing)] = "s"
            else:
                sList[wlindex.index(thing)] = ""
        print(f"You have won {won} game{sList[0]} and lost {lost} game{sList[1]}.")
        drawcards()
    else:
        print("Not enough cards, reshuffling")
        createDeck()
createDeck()
while True:
    thingy = input("Enter R to reshuffle the deck, or press enter to play again without reshuffling.\n")
    print(thingy.upper())
    if thingy.upper() == "R":
        createDeck()
        gameloop()
    else:
        gameloop()
