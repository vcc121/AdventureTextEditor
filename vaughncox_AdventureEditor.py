import json

def main():
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        userChoice = getUserChoice()
        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            print("Load default game")
            game = getDefaultGame()
        elif userChoice == "2":
            print("Load game file")
            game = loadGame()
        elif userChoice == "3":
            print("Save current game")
            saveGame(game)
        elif userChoice == "4":
            print("Edit or add node")
            editNode(game)
        elif userChoice == "5":
            print("Play current game")
            playGame(game)
        else:
            print("Invalid input, please choose again.")
                  
def getUserChoice():
    print("""
        1. Load default game
        2. Load a game file
        3. Save the current game
        4. Edit or add a node
        5. Play current game
        0. Exit
         """)
    userChoice = input("What will you do? ")
    return userChoice

def getDefaultGame():
     game = {"start": ["default start node", "Start over", "start", "Quit", "quit"]}
     return game
    
def saveGame(game):
    fileOut = open("game.json", "w")
    game = json.dump(game, fileOut)
    fileOut.close()
    print("Game saved!")

def loadGame():
    fileIn = open("game.json", "r")
    game = json.load(fileIn)
    
    print("Game loaded!")
    return game

def playGame(game):
    keepGoing = True
    currentNode = "start"
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)
            



def playNode(game, currentNode):
    if currentNode in game.keys():
        (description, menu1, node1, menu2, node2) = game[currentNode]
        print(f"""
        {description}

        1. {menu1} 
        2. {menu2} 
        """)
        userChoice = input("Which will you do? ")
        if userChoice == "1":
            nextNode = node1
        elif userChoice == "2":
            nextNode = node2
        else:
            nextNode = currentNode
            print("Please choose 1 or 2")
            
        return nextNode
    
def editNode(game):
    print("Current status of game: ")
    print(json.dumps(game, indent=2))
    
    print ("Existing node names: ")
    for nodeName in game.keys():
        print(f" {nodeName}")
    
    newNodeName = input("Name of node to edit or create? ")
    if newNodeName in game.keys():
        newContent = game[newNodeName]
    else:
        newContent =  ["", "", "", "", ""]
    
    (description, menu1, menu2, node1, node2) = newContent
    newDesc = editField("description", description)
    newMenu1 = editField("Menu 1", menu1)
    newNode1 = editField("Node 1", node1)
    newMenu2 = editField("Menu 2", menu2)
    newNode2 = editField("Node 2", node2)
    
    game[newNodeName] = [newDesc, newMenu1, newNode1, newMenu2, newNode2]
    
def editField(prompt, currentValue):
    newValue = input(f"{prompt} ({currentValue}): ")
    if newValue == "":
        newValue = currentValue
        
    return newValue

main()