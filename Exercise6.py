#Game- Snake, Water, gun
print("\t\t\t\t\tWelcome, Try your luck by playing Snake, water, gun\t\t\t\t\t")
print("\t\t\t\t\tyou have 10 chances\t\t\t\t\t")
S="SNAKE"
W="WATER"
G="GUN"
user=0
cpu=0
num=input("\t\t\t\t\tPress Y to start N to exit: ")
def game():
  lst=[S,W,G]

  i=0
  global user
  global cpu


  if num=="Y" or num=="y" :

    while i<10:
       import random
       choice=random.choice(lst)
       user1=input("Enter  S for SNAKE W for WATER G for GUN: ")
       if (user1=="S" or user1=="s") and choice==W:
         a=f"user1: SNAKE CPU:{choice}"
         print(a)
         user+=1
         print(f"user {user} cpu {cpu}")

       elif (user1=="S" or user1=="s") and choice==G:
           a = f"user1: SNAKE CPU:{choice}"
           print(a)
           cpu+=1
           print(f"user {user} cpu {cpu}")

       elif (user1 == "G" or user1=="g") and choice == S:
           a = f"user1: GUN CPU:{choice}"
           print(a)
           user+=1
           print(f"user {user} cpu {cpu}")
       elif user1 == ("G" or user1=="g") and choice == W:
           a = f"user1: GUN CPU:{choice}"
           print(a)
           cpu+=1
           print(f"user {user} cpu {cpu}")
       elif (user1 == "W" or user1=="w")  and choice == G:
           a = f"user1: WATER CPU:{choice}"
           print(a)
           user+=1
           print(f"user {user} cpu {cpu}")
       elif (user1 == "W" or user1=="w")  and choice == S:
           a = f"user1: WATER CPU:{choice}"
           print(a)
           cpu+=1
           print(f"user {user} cpu {cpu}")
       else:
           if user1=="S" or user1=="s":
             print("DRAW, you both chose snake")
             user+=0.5
             cpu+=0.5
             print(f"user {user} cpu {cpu}")

           elif user1=="W" or user1=="w":
             print("DRAW,you both chose water")
             user+=0.5
             cpu+=0.5
             print(f"user {user} cpu {cpu}")

           elif user1=="G" or user1=="g":
             print("DRAW, you both chose gun")
             user+=0.5
             cpu+=0.5
             print(f"user {user} cpu {cpu}")
           else:
               print("wrong input : try again")
       i=i+1

  elif num=="N" or num=="n":
    print("\t\t\t\t\tThank you, keep visiting")
  else:
      print("please enter the correct input")
      game()
game()
if num=="Y" or num=="y":
   z=input("Do you want to CONTINUE: Enter Y for yes or Enter any key to exit: ")
   while z=="Y" or z=="y" :
      game()
      z=input("do you want to play more : Enter Y for yes or print any key to exit:  ")
   if z!='y' or z!='Y':
      print("Thank you")
      if user>cpu:
        print(f"USER: {user}  CPU:{cpu}" )
        print("congrats,you won")
      elif user<cpu:
        print(f"USER: {user}  CPU:{cpu}")
        print("sorry, you loose")
      else:
        print(f"USER: {user}  CPU:{cpu}")
        print("GAME DRAW")

        print("\t\t\t\t\tThank you, keep visiting")

