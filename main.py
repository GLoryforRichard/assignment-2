# Import the random library to use for the dice later
import sys
import random

# Put all the functions into another file and import them
import function

# Import hero
import hero

# Import monster
import monster

# Import os module
import os

# Assignment 2
# Q5 Make a class called Character to serve as a parent class


class Character:
    # private propety
    __combat_strength = 0
    __health_points = 0

    # Init method (constructor)
    def __init__(self):
        self.__combat_strength = random.randint(1, 20)
        self.__health_points = random.randint(50, 100)

    # Combat Strength Property
    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        print('combat_strength Setted to {}'.format(value))
        self.__combat_strength = value

    @combat_strength.deleter
    def combat_strength(self):
        print("combat_strength is deleted")
        del self.__combat_strength

    # Health Points Property
    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        print('health_points Setted to {}'.format(value))
        self.__health_points = value

    @health_points.deleter
    def health_points(self):
        print("health_points is deleted")
        del self.__health_points

    # Del method (destructor)
    def __del__(self):
        print("The character object is being destroyed by the garbage collector")

# Q6 Refactor the Hero class and the Monster class


class Hero(Character):
    def __init__(self):
        Character.__init__(self)


class Monster(Character):
    def __init__(self):
        Character.__init__(self)


# Q10 Use the os library/module from python to print out the operating system name of the computer it’s running on
system_type = os.name
if(system_type == 'posix'):
    print("    Your system is Linux,Unix or Mac OS\n")
elif(system_type == 'nt'):
    print("    Your system name is Windows\n")
else:
    print("    Get system infomation error\n")
# Q11 Use the platform library/module from python to find a function that helps you print out the version of python.
print("    Python version")
print("    "+sys.version+"\n")

# Call your Test Functions
print("    |  Testing functions.py")
print("    ------------------------------------------------------------------")
function.test_use_loot()
function.test_collect_loot()
function.test_hero_attacks()
function.test_monster_attacks()
function.test_final_score()
print("    |  Done Testing")
print("    ------------------------------------------------------------------")


# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion",
                "Secret Note", "Leather Boots", "Flimsy Gloves"]

# Maximum Items that can be held in the Belt is 5
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the Monster's Features
monster_features = {
    "Spikes": 1,
    "Big Tail": 3,
    "Sharp Teeth": 5
}

# Define the number of stars to award the player
num_stars = 0
input_valid = False

# If Save Exists, Load the game to continue from the last save
# Lab 7 - With keyword automatically calls close() for you, once it exits the block
# Lab 7 - With keyword with append and reading (If you open for reading only, gives an error No File Exists)
with open("save.txt", "a+") as save_file:
    # If the file is not empty, Load it
    if save_file.readline():
        print("    ------------------------------------------------------------------")
        print("    |    Loading your saved game...")
        combat_strength = int(save_file.readline())
        print("    |    Loaded combat strength is: " + str(combat_strength))
        health_points = int(save_file.readline())
        print("    |    Loaded health points is: " + str(health_points))
        # Lab 6 - Answer 6
        who_won_last = str(save_file.readline())
        print("    |    " + who_won_last)
        print("    ------------------------------------------------------------------")
    else:
        # Otherwise - Get user input for Hero's combat strength, weapon and health points
        # Loop to get valid input for Hero Combat Strength
        i = 0
        while not input_valid and i in range(5):
            print(
                "    ------------------------------------------------------------------")
            print("    |", end="    ")
            combat_strength = input("Enter your combat Strength (1-6): ")

            # Validate input: Check if the string inputted is numeric
            if not combat_strength.isnumeric():
                # If one of the inputs are invalid, print error message and halt
                print(
                    "    |    TRY AGAIN: Player needs to enter integer numbers for Combat Strength    |")
                i = i + 1

            # Note: Now safe to cast combat_strength to integer
            # Validate input: Check if the string inputted
            elif int(combat_strength) not in range(1, 7):
                print("    |    TRY AGAIN: Enter a valid integer between 1 and 6 only")
                i = i + 1

            else:
                input_valid = True

        if input_valid:
            # Input was valid - broke out of while loop
            combat_strength = int(combat_strength)

            # Roll for weapon
            print("    |", end="    ")
            input("Roll the dice for your weapon (Press enter)")
            ascii_image5 = """
                      , %               .           
           *      @./  #         @  &.(         
          @        /@   (      ,    @       # @ 
          @        ..@#% @     @&*#@(         % 
           &   (  @    (   / /   *    @  .   /  
             @ % #         /   .       @ ( @    
                         %   .@*                
                       #         .              
                     /     # @   *              
                         ,     %                
                    @&@           @&@
                    """
            print(ascii_image5)
            weapon_roll = random.choice(small_dice_options)

            # Limit the combat strength to 6
            combat_strength = min(6, (combat_strength + weapon_roll))
            print("    |    The hero\'s weapon is " +
                  str(weapons[weapon_roll - 1]))

            # Roll for player health points
            print("    |", end="    ")
            input("Roll the dice for your health points (Press enter)")
            health_points = 20  # random.choice(big_dice_options)
            print("    |    Player rolled " +
                  str(health_points) + " health points")

# Roll for monster combat strength
print("    |", end="    ")
input("Roll the dice for the monster's combat strength (Press enter)")
m_combat_strength = 1  # random.choice(big_dice_options)
print("    |    Player rolled " + str(m_combat_strength) +
      " combat strength for the monster")

# Roll for monster health points
print("    |", end="    ")
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = 1  # random.choice(big_dice_options)
print("    |    Player rolled " + str(m_health_points) +
      " health points for the monster")

# Roll for the monster's power
print("    |", end="    ")
input("Roll for Monster's Magic Power (Press enter)")
ascii_image4 = """
            @%   @                      
     @     @                        
         &                          
  @      .                          

 @       @                    @     
          @                  @      
  @         @              @  @     
   @            ,@@@@@@@     @      
     @                     @        
        @               @           
             @@@@@@@                

                                  """
print(ascii_image4)
power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])
print("    |    The monster's magic power is now: " + power_roll)

# Roll for the Monster's Features
input("    |    Roll for the Monster's Features (Press enter)")
feature_roll = random.choice(["Spikes", "Big Tail", "Sharp Teeth"])

# Increase the monster’s Combat Strength by its Power
m_combat_strength = min(6, m_combat_strength + monster_powers[power_roll])
print("    |    The monster's combat strength is now " +
      str(m_combat_strength) + " because of it's " + power_roll + " power")

# Increase the monster’s Health Points by its Feature
m_health_points = min(20, m_health_points + monster_features[feature_roll])
print("    |    The monster's health points is now " +
      str(m_health_points) + " because of it's " + feature_roll + " feature")

# Collect Loot
print("    ------------------------------------------------------------------")
print("    |    !!You find a loot bag!! You look inside to find 2 items:")
print("    |", end="    ")
input("Roll for first item (Press enter)")
# Lab 7 - Don't need to return belt list, because it was passed by reference
function.collect_loot(loot_options, belt)
print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Roll for second item (Press enter)")
# Lab 7 - Don't need to return belt list, because it was passed by reference
function.collect_loot(loot_options, belt)

# Use Loot
print("    |    !!You see a monster in the distance! So you quickly use an item:")
# Lab 7 - Don't need to return belt list, because it was passed by reference
health_points = function.use_loot(belt, health_points)

# Call Recursive function to go down dream levels
# Go Crazy -> Lose Health, Gain Strength
print("    ------------------------------------------------------------------")
print("    |", end="    ")
print("꧁༺CAUTION, DREAMING DAMAGES YOUR HEALTH!༻꧂")
# Lab 7 - Validate the number of dream levels entered
i = 0
input_invalid = True
while input_invalid and i in range(5):
    num_dream_lvls = input(
        "    |    How many dream levels do you want to go down? ")
    if not num_dream_lvls.isnumeric():
        print("    |    TRY AGAIN: Player needs to enter integer numbers num dream levels")
        i = i + 1
    elif int(num_dream_lvls) <= -1:
        print("    |    TRY AGAIN: Player needs to enter a positive number for num dream levels")
    else:
        num_dream_lvls = int(num_dream_lvls)
        input_invalid = False

if num_dream_lvls != 0:
    health_points = max(0, health_points - 5)
    crazy_level = function.inception_dream(num_dream_lvls)
    combat_strength = min(6, combat_strength + int(crazy_level))
    print("    |    Your combat strength is now increased to: " + str(combat_strength))
    print("    |    Your health points are now reduced to: " + str(health_points))

# Loop while the monster and the player are alive. Call fight sequence functions
print("    ------------------------------------------------------------------")
while m_health_points > 0 and health_points > 0:
    # Fight Sequence
    print("    |", end="    ")

    # Who attacks first?
    input("Roll to see who attacks first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if not (attack_roll % 2 == 0):
        print("    ------------------------------------------------------------------")
        print("    |", end="    ")
        input("You strike (Press enter)")
        # Hero Attacks First
        m_health_points = function.hero_attacks(
            combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
        else:
            print(
                "    ------------------------------------------------------------------")
            print("    |", end="    ")
            input("The monster strikes (Press enter)!!!")
            # Monster Attacks Back
            health_points = function.monster_attacks(
                m_combat_strength, health_points)
            if health_points == 0:
                num_stars = 1
            else:
                num_stars = 2

                # If you have more items on your belt, use them
                if belt:
                    # Lab 7 - Don't need to return belt list, because it was passed by reference above
                    health_points = function.use_loot(belt, health_points)

    else:
        print("    ------------------------------------------------------------------")
        print("    |", end="    ")
        # Monster Attacks First
        input("The Monster strikes (Press enter)")
        health_points = function.monster_attacks(
            m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            print("------------------------------------------------------------------")
            print("    |", end="    ")
            input("The hero strikes!! (Press enter)")
            # Hero Attacks Back
            m_health_points = function.hero_attacks(
                combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3
            else:
                num_stars = 2

            # If you have more items on your belt, use them
            if belt:
                # Lab 7 - Don't need to return belt list, because it was passed by reference above
                health_points = function.use_loot(belt, health_points)

# Final Score Display
function.final_score(num_stars)

# Lab 7: Save the game if the Hero killed the Monster and the Hero is still alive
if m_health_points == 0 and health_points > 0:
    # Lab 7 - With keyword and write mode, will overwrite the file if it already exists, or create a new file.
    with open("save.txt", "w") as save_file:
        print("Saving your Game...")
        save_file.write("Most Recent Save\n")
        save_file.write(str(combat_strength) + "\n")
        save_file.write(str(health_points) + "\n")
        # Lab 6 - Answer 5
        save_file.write("Hero has killed a monster\n")

# Lab 7 - We don't need to close the File
