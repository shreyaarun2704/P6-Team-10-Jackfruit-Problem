import random
import turtle
import time


def draw_dice(number):
                                     
    turtle.clear()
    turtle.pensize(3)
    turtle.color("black")
    turtle.fillcolor("white")
    turtle.begin_fill()

    turtle.penup()
    turtle.back(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
                                                       
    dots = {
        1: [(0, 0)],
        2: [(-30, 30), (30, -30)],
        3: [(-30, 30), (0, 0), (30, -30)],
        4: [(-30, 30), (-30, -30), (30, 30), (30, -30)],
        5: [(-30, 30), (-30, -30), (0, 0), (30, 30), (30, -30)],
        6: [(-30, 30), (-30, 0), (-30, -30), (30, 30), (30, 0), (30, -30)]
    }

    turtle.penup()

    for (x, y) in dots[number]:
        turtle.goto(x, y)
        turtle.penup()
        turtle.dot(15)
        turtle.penup()

        
def user_guess_number(numberofrolls):
    
    global user_guesses
    
    for i in range(numberofrolls):
        user_guess=input("Enter your guess(1-6) :")
        
        if user_guess in ['1','2','3','4','5','6']:
             user_guesses.append(int(user_guess))
             
        else:
            print("Enter number from 1-6 only ")
            user_guess_number(numberofrolls-1)
            
    return user_guesses   



def diceroll(n):
        time.sleep(3)
        draw_dice(n)
        turtle.hideturtle()
        turtle.goto(0, 0)
        time.sleep(.5)
	time.sleep(1)
        turtle.clear()

        
def gameplay(numberofrolls,diceroll,user_guess_number):
        print()
        print("Menu")                               #Creating user interface
        print("1.Roll dices")
        print("2.Gamble")
        print()
        user_choice=input("Enter 1 or 2:")
        print()
        correct_guess=0
        
        if user_choice=='1':                         #Roll only mode
            for i in range(numberofrolls):
                n=random.randint(1,6)
                diceroll(n)
                dicerollvalues.append(n)
                print(f"The number on die {i+1} is {n}")
                
        elif user_choice=='2':                               #Gamble mode
            list_guess=user_guess_number(numberofrolls)
            
            for i in range(numberofrolls):
                n=random.randint(1,6)
                dicerollvalues.append(n)
                
                if list_guess[i]==n:
                    print(f"You guessed the number  correctly!")
                    correct_guess+=1
                    
                else:
                    print(f"You guessed {list_guess[i]}  wrong")
              
                print(f"The number on the die {i+1} is {n}")
                diceroll(n)
                
        else:
            print("Please enter valid choice")
            gameplay(numberofrolls,diceroll,user_guess_number)
        return correct_guess

    
def statistics(numberofrolls,correct_guesses,dicerollvalues):
        print("\n----- GAME STATISTICS -----")
        # Count frequency of each roll number from 1 to 6
        roll_counts = {i: 0 for i in range(1, 7)}
        for i in roll_counts:
            for k in dicerollvalues:
                if i==k:
                    roll_counts[i]+=1

        # Print roll frequencies
        print("\nNumber Frequency of Rolls:")
        for key, value in roll_counts.items():
            print(f"{key}: {value} times")
            
        if len(user_guesses) > 0:
            accuracy = (correct_guesses / numberofrolls) * 100
            print(f"\nCorrect Guesses: {correct_guesses}/{numberofrolls}")
            print(f"Accuracy: {accuracy:.2f}%")
                  
        else:
            print("\nNo guesses made. You selected Roll Only mode.")
                
                        
user_guesses=[]
dicerollvalues=[]
numberofrolls= int(input('Enter How Many Times You Want to Roll The Dice: '))
        
turtle.speed(2)
turtle.hideturtle()
correct_guesses=gameplay(numberofrolls,diceroll,user_guess_number)
statistics(numberofrolls,correct_guesses,dicerollvalues)

turtle.done()
