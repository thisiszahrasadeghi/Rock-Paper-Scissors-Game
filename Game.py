import random


rock = r'''                               
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

               '''
                     

paper = r'''    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

                '''

scissors = r'''    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
                '''


user_choice = int(input("what do you choose? Type 0 for \"Rock\" , 1 for \"Paper\" and 2 for \"Scissors\" ."))
game_images = [rock , paper , scissors ]

if user_choice <= 2:
    
    print(game_images[user_choice])
    
    computer_choice = random.randint(0,2)
    print("Computer Choice :")
    print(game_images[computer_choice])


    if user_choice == 0:
        if computer_choice == 0 :
            print("TRY AGAIN")
        elif computer_choice == 1 :
            print("YOU LOSE")
        else :
            print("YOU WIN")
    
    if user_choice == 1:
        if computer_choice == 0 :
            print("YOU WIN")
        elif computer_choice == 1 :
            print("TRY AGAIN")
        else :
            print("YOU LOSE")
    
    if user_choice == 2:
        if computer_choice == 0 :
            print("YOU LOSE")
        elif computer_choice == 1 :
            print("YOU WIN")
        else :
            print("TRY AGAIN")

else :
    print("Please choose 0 , 1 or 2.")
