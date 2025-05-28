'''
1 for snake 
-1 for water 
0 for gun
'''

import random

def determined_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Its a tie!!"
    elif(user_choice == 'snake' and comp_choice =='water') or \
        (user_choice == 'water' and comp_choice =='gun') or \
        (user_choice == 'gun' and comp_choice =='snake') :
        return "yOu Win!!!"
    else:
        return "computer wins!!"
    
def snake_water_gun_game():
    choice = ['snake', 'water', 'gun']
    
    print("Welcome to the game !!!")
    
    while True:
        print("\nChoose one: Snake, water, or Gun")
        user_choice = input("Your Choice : ").lower()
        
        if user_choice not in choice :
            print("Invalid choice !!!!")
            continue
        
        comp_choice = random.choice(choice)
        print(f"Computer chose : {comp_choice}")
        
        result =determined_winner(user_choice, comp_choice)
        print(result)
        
        play_again = input("Do you want to play again ? (yes/no) : ").lower()
        if play_again  != 'yes' :
            break
        
        print("Thanks for plying !")
        
snake_water_gun_game()        