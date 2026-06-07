# 1. Ler resumo sobre as classes
# 2. Criar party
# 3. Ver histórico de pontuação
# 4. Carregar jogo salvo
# 5. Jogar

import os

def star_menu():
    while True:
        print("Hello! Welcome to Python & Dragons")
        print("What do you want to do:-\n")
        print("-> 1. Learn about this game")
        print("-> 2. Learng about classes")
        print("-> 3. Create my party")
        print("-> 4. Load saved game")
        print("-> 5. Score history")
        print("-> 6. Play")
        print("-> 7. Quit")
        print("chat with system:-",end=' ')
        
        player_action = int(input())
      
        if player_action == 1:
            game_instructions()   
        
        elif player_action == 2:
            classes_disclosure() 
            
        elif player_action == 3:
            create_party() 
        
        elif player_action == 4:
            load_game()
                
        elif player_action == 5:
            show_history()
        
        elif player_action == 6:
            start_game()
        
        elif player_action == 7:
            print("Thank you for playing!\n")         
            print("Leaving the game\n")
            print("...")
        
        break
        
def game_instructions():  
    return

def classes_disclosure():
    return 
            
def create_party():
    return
         
def load_game():
    return 
                
def show_history():
    return 
        
def start_game():
    print("Have you created a party? (Y/N)")
    answer = input()
    
    if answer == 'Y' or answer == 'y':
        game = Game ()
    
    elif answer == 'N' or answer == 'n':
        print("Ok, we should create a party first!\n")
        create_party() 