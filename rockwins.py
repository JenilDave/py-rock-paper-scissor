import random
if __name__ == "__main__":
    me = 0
    he = 0
    while True:
        matches = int(input("Enter number of matches to play series: "))
        if matches%2 == 0:
            print("Error: Please enter Odd number only for better evaluation")
            continue
        break
    winner = False
    for i in range(matches):
        winner = False
        print("Lets play Game number: " ,i+1)
        while winner == False:
            __type = int(input("Enter respectively:\n1: Rock\n2: Scissor\n3: Paper\n"))
            auto = random.randint(1,3)
            if (__type == 1 and auto == 2) or (__type == 2 and auto == 3) or (__type == 3 and auto == 1):
                print("You have won this match!!!, Computer did ",auto)
                me +=1
            elif (__type == 2 and auto == 1) or (__type == 3 and auto == 2) or (__type == 1 and auto == 3):
                print("Computer has won this match, it did ", auto)
                he +=1
            else:
                print("\nNo result, lets try again.\nYou did ",__type,"Comp did ",auto)
            if (me >= 1 or he >= 1):
                if me == int(matches/2)+1:
                    print("You have won the series !!!\n")
                elif he == int(matches/2)+1:
                    print("Computer has won the series\n")
                winner = True
            print("\nYOUR POINTS: ",me,"\nCOMP POINTS: ",he)
