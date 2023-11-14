import time
def start_game():
    print("Welcome to the Princess Rescue Adventure!")
    print("You are a brave knight on a quest to rescue the kidnapped princess.")
    time.sleep(1)
    print("You stand at a crossroad. Two paths lead to the villain's castle.")
    print("1. Take the forest path.")
    print("2. Take the mountain path.")    
    choice = input("Enter your choice (1/2): ")    
    if choice == "1":
        forest_path()
    elif choice == "2":
        mountain_path()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        start_game()
def forest_path():
    print("You venture into the enchanted forest filled with magical creatures.")
    time.sleep(1)
    print("You come across a talking owl that offers guidance.")
    print("1. Follow the owl's advice.")
    print("2. Ignore the owl and continue on your own.")    
    choice = input("Enter your choice (1/2): ")    
    if choice == "1":
        follow_owl()
    elif choice == "2":
        continue_alone()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        forest_path()
def mountain_path():
    print("You climb the treacherous mountain path, facing strong winds and steep cliffs.")
    time.sleep(1)
    print("You find a magical flying carpet that can speed up your journey.")
    print("1. Use the flying carpet.")
    print("2. Continue climbing without the carpet.")   
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        use_flying_carpet()
    elif choice == "2":
        continue_climbing()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        mountain_path()
def follow_owl():
    print("You follow the owl's guidance and discover a hidden shortcut.")
    time.sleep(1)
    print("The shortcut leads you to the castle gates without any trouble.")
    print("You have arrived at the villain's castle!")
    rescue_princess()
def continue_alone():
    print("You decide to continue on your own, facing challenges in the forest.")
    time.sleep(1)
    print("Unfortunately, you get lost and waste precious time.")
    print("Your journey becomes more perilous.")
    continue_journey()
def use_flying_carpet():
    print("You use the flying carpet to soar through the skies.")
    time.sleep(1)
    print("The journey becomes swift, and you reach the castle in record time.")
    print("You have arrived at the villain's castle!")
    rescue_princess()
def continue_climbing():
    print("You continue climbing the mountain without the carpet.")
    time.sleep(1)
    print("The journey is tough, but you reach the castle, exhausted but determined.")
    print("You have arrived at the villain's castle!")
    rescue_princess()
def rescue_princess():
    print("You face the villain in a fierce battle and rescue the princess.")
    print("Congratulations, brave knight! You've completed your quest and saved the day!")
def continue_journey():
    print("Your journey continues as you face more challenges.")
    print("The outcome of your adventure is uncertain. Good luck!")
if __name__ == "__main__":
    start_game()
