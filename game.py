import yaml
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

themes = {
    "1": "Fantasy",
    "2": "Mystery",
    "3": "Romance",
    "4": "Comedy"
}

def choose_theme():
    print("\nChoose your adventure theme:\n")
    for key, value in themes.items():
        print(f"{key}) {value}")
    choice = input("\n> ")
    return themes.get(choice, "Fantasy")  # Default to Fantasy


# Utility Functions
def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_title():
    print(Fore.RED + Style.BRIGHT + r"""  

                                                                    
                    🔥 The Ember Stone 🔥
          
  ______     __  __     ____     ______     _____       
 |  ____|   |  \/  |   |  _ \   |  ____|   |  __ \    
 | |__      | \  / |   | |_) |  | |__      | |__) |    
 |  __|     | |\/| |   |  _ <   |  __|     |  _  /   
 | |____    | |  | |   | |_) |  | |____    | | \ \   
 |______|   |_|  |_|   |____/   |______|   |_|  \_\        
          

    _____ _______ ____  _   _ ______ 
   / ____|__   __/ __ \| \ | |  ____|
  | (___    | | | |  | |  \| | |__   
   \___ \   | | | |  | | . ` |  __|  
   ____) |  | | | |__| | |\  | |____ 
  |_____/   |_|  \____/|_| \_|______|
""")
    

print(Fore.RED + Style.BRIGHT + r""" 
    
 ___  __        __   ___  __               ___       ___     ___  __   __  
|__  /  ` |__| /  \ |__  /__`    | |\ |     |  |__| |__     |__  /  \ / _` 
|___ \__, |  | \__/ |___ .__/    | | \|     |  |  | |___    |    \__/ \__> 
                                                                           
""")

def scene_break():
    print(Fore.WHITE + "\n" + "-" * 50 + "\n")

def load_story(filename="story.yaml"):
    with open(filename, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def play_game(story, start="scene_1"):
    current = start
    while current in story:
        scene = story[current]
        scene_break()
        slow_print(Fore.YELLOW + scene["text"])
        if "choices" not in scene:
            break
        scene_break()
        for key, choice in scene["choices"].items():
            print(Fore.GREEN + f"{key}) {choice.split('->')[0].strip()}")
        selection = input(Fore.CYAN + "> ")
        # Convert choice keys to strings for comparison
        choices = {str(k): v for k, v in scene["choices"].items()}
        if selection in choices:
            next_scene = choices[selection].split("->")[1].strip()
            current = next_scene
        else:
            print(Fore.RED + "Invalid choice. Try again.")


if __name__ == "__main__":
    show_title()
    
    selected_theme = choose_theme()
    story = load_story(f"{selected_theme.lower()}.yaml")
    play_game(story)
