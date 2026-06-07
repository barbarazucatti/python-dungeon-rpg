# 1. Ler resumo sobre as classes
# 2. Criar party
# 3. Ver histórico de pontuação
# 4. Carregar jogo salvo
# 5. Jogar

import os

def start_menu():
    while True:
        print(" ")
        print("Hello! Welcome to Python & Dragons")
        print("What do you want to do:-\n")
        print("->📖 1. Learn about this game")
        print("->🧙 2. Learng about classes")
        print("->⚔️  3. Create my party")
        print("->💾 4. Load game")
        print("->🏆 5. Score history")
        print("->🎲 6. Play")
        print("->🚪 7. Quit")
        print()
        
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
    BOLD = "\033[1m"
    RESET = "\033[0m"
    BRIGHT_WHITE = "\033[97m"
    CYAN = "\033[36m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_YELLOW = "\033[93m"

    print(f"""

=================================
      {BOLD}{CYAN} 🐍 PYTHON & DRAGONS 🐉 {RESET}{RESET}
=================================

{BOLD}{BRIGHT_YELLOW}Welcome{RESET}, adventurer!

Your mission is simple: {BOLD}enter a dangerous dungeon and defeat the
3 bosses that await your party.{RESET}

If all of your heroes {RED}{BOLD}fall{RESET}{RESET} in battle, the adventure ends in {RED}{BOLD}defeat{RESET}{RESET}.

However, if you manage to {GREEN}{BOLD}defeat the final boss{RESET}{RESET}, even with only
one hero standing, {GREEN}{BOLD}victory is yours!{RESET}{RESET}

{BOLD}{BRIGHT_BLUE}GAMEPLAY{RESET}{RESET}

The game is turn-based. During each round, heroes and enemies
take turns performing actions.

After defeating a boss, your party advances deeper into the dungeon
and gains experience, becoming stronger for the challenges ahead.

Heroes can also recover health by resting:

- 1 turn of rest restores {BOLD}50% of missing health{RESET}
- 2 turns of rest {BOLD}fully restore health{RESET}

Choose carefully when to fight and when to recover.

{BOLD}{BRIGHT_BLUE}COMBAT & DICE{RESET}{RESET}

Combat outcomes are determined by a 10-sided die.

A {BOLD}low roll{RESET} may cause an attack to {RED}{BOLD}fail{RESET}{RESET}, while a {BOLD}high roll{RESET}
increases its {GREEN}{BOLD}effectiveness{RESET}{RESET}.

The higher the roll, the greater the chance of dealing
significant damage or successfully performing a skill.

Luck matters, but strategy matters even more.

{BOLD}{BRIGHT_BLUE}BUILD YOUR PARTY{RESET}{RESET}

Before starting your adventure, you must create a party of 3 heroes.

Available classes:

- ⚔️ Fighter
- 🧙 Wizard
- 🛡️ Cleric
- 🗡️ Rogue

Each hero can be customized with different skills and equipment.

Your choices will shape your strategy throughout the dungeon.

{BOLD}{BRIGHT_BLUE}DIFFICULTY{RESET}{RESET}

You may choose the dungeon difficulty before the adventure begins.

Higher difficulties feature stronger enemies and more dangerous
encounters, but offer a greater challenge for experienced adventurers.

{BRIGHT_YELLOW}{BOLD}Good luck, hero.{RESET}{RESET}

{BRIGHT_YELLOW}{BOLD}The dungeon awaits...{RESET}{RESET}

""")

    input("Press Enter to return to the menu...\n")

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
        game = game
    
    elif answer == 'N' or answer == 'n':
        print("Ok, we should create a party first!\n")
        create_party()


start_menu()
 