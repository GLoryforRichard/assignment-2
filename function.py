# Import the random library to use for the dice later
import random


# Lab 7 - Belt is passed by reference because it is a list
def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]
    item_num = 0

    # Validate Arguments belt and health points
    if len(belt) <= 0 or len(belt) > 5:
        print("    | You cannot use loot with an empty belt, and you can't have more than 5 items on your belt")
    elif health_points <= 0 or health_points > 20:
        print("    | You cannot use loot if you're dead, and you can't have more than 20 health points")
    else:
        # Choose the loot to use
        # Lab 7 - Added a choice to use nothing from the belt
        print("    |    Enter -1 : to use nothing")
        for item_option in belt:
            print("    |    Enter " + str(item_num) + " : to use " + item_option)
            item_num += 1
        # Lab 7 - Validate the item number entered
        i = 0
        input_invalid = True
        use_an_item = False
        while input_invalid and i in range(5):
            item_choice = input("    |    Choose which item from your belt to use (Enter a Number):  ")
            if item_choice == "-1":
                print("    |    Skipping Using Loot")
                input_invalid = False
            elif not item_choice.isnumeric():
                print("    |    TRY AGAIN: Item number entered must be a number")
            else:
                item_choice = int(item_choice)
                item = belt.pop(item_choice)
                use_an_item = True
                input_invalid = False

        # If Item number was valid, Determine consequence of loot chosen
        if use_an_item and not input_invalid:
            if item in good_loot_options:
                health_points = min(20, (health_points + 2))
                print("    |    You used " + item + " to increase your health to " + str(health_points))
            elif item in bad_loot_options:
                health_points = max(0, (health_points - 2))
                print("    |    You used " + item + " to reduce your health to " + str(health_points))
            else:
                print("    |    You used " + item + " but it's not helpful")
    # Lab 7 - Don't need to return belt list, because it was passed by reference above
    return health_points


# Lab 7 - Loot options and Belt is passed by reference because they are lists
def collect_loot(loot_options, belt):
    if len(loot_options) <= 0:
        print("    | Loot options can't be empty. There must exist a loot option to roll for")
    elif len(belt) > 5:
        print("    | Belt is full. Cannot add any more loot.")
    else:
        ascii_image3 = """
                          @@@ @@                
                 *# ,        @              
               @           @                
                    @@@@@@@@                
                   @   @ @% @*              
                @     @   ,    &@           
              @                   @         
             @                     @        
            @                       @       
            @                       @       
            @*                     @        
              @                  @@         
                  @@@@@@@@@@@@          
                  """
        print(ascii_image3)
        loot_roll = random.choice(range(1, len(loot_options) + 1))
        loot = loot_options.pop(loot_roll - 1)
        belt.append(loot)
        print("    |    Your belt: ", belt)
        # Lab 7 - Don't need to return belt list, because it was passed by reference above
    return


# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    if combat_strength <= 0 or combat_strength >= 7:
        print("    | Hero cannot fight with 0 combat strength. Cannot exceeds maximum strength of6")
    elif m_health_points < 1 or m_health_points > 20:
        print("    | Monster must be alive, and not exceed the maximum health points 20")
    else:
        ascii_image = """
                                    @@   @@ 
                                    @    @  
                                    @   @   
                   @@@@@@          @@  @    
                @@       @@        @ @@     
               @%         @     @@@ @       
                @        @@     @@@@@     
                   @@@@@        @@       
                   @    @@@@                
              @@@ @@                        
           @@     @                         
       @@*       @                          
       @        @@                          
               @@                                                    
             @   @@@@@@@                    
            @            @                  
          @              @                  

      """
        print(ascii_image)
        print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
        if combat_strength >= m_health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            m_health_points -= combat_strength

            print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    if m_combat_strength <= 0 or m_combat_strength >= 7:
        print("    | Monster cannot fight with 0 combat strength. Cannot exceeds maximum strength of6")
    elif health_points < 1 or health_points > 20:
        print("    | Hero must be alive, and not exceed the maximum health points 20")
    else:
        ascii_image2 = """                                                                 
               @@@@ @                           
          (     @*&@  ,                         
        @               %                       
         &#(@(@%@@@@@*   /                      
          @@@@@.                                
                   @       /                    
                    %         @                 
                ,(@(*/           %              
                   @ (  .@#                 @   
                              @           .@@. @
                       @         ,              
                          @       @ .@          
                                 @              
                              *(*  *      
                 """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
        if m_combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            health_points -= m_combat_strength
            print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points


# Gets and Validates the Hero's name, and Awards number of Stars
def final_score(num_stars):
    if num_stars <= -1 or num_stars > 3:
        print("    | Lower than the min num stars 0, or Exceeds the maximum number of stars allowed 3")
    else:
        tries = 0
        input_invalid = True
        while input_invalid and tries in range(5):
            print("    |", end="    ")
            hero_name = input("Enter your Hero's name (in two words)")
            name = hero_name.split()
            if len(name) != 2:
                print("    |    TRY AGAIN: Please enter a name with two parts (separated by a space)")
                tries += 1
            else:
                if not name[0].isalpha() or not name[1].isalpha():
                    print("    |    TRY AGAIN: Please enter an alphabetical name")
                else:
                    short_name = name[0][0:2] + name[1][0:1]
                    print("    |    I'm going to call you " + short_name + " for short")
                    input_invalid = False

        if not input_invalid:
            stars = "*" * num_stars
            print("    |    Hero " + short_name + " gets <" + stars + "> stars")
    return


# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    # Base case
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 0:
        print("    |    You are in the deepest dream level now")
        print("    |    You start to regress back through your dreams to real life.")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        return 2

    # Recursive case:
    # Decrement the counter to go deeper into the dream levels and reach base.
    else:
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + inception_dream(1)
        # 1 + 1 + 1 + 1 + 1 + inception_dream(0)
        # base case: 1 + 1 + 1 + 1 + 1 + 2
        # Combine return value with something already existing in the return
        return 1 + int(inception_dream(num_dream_lvls - 1))


# Test Functions
def test_use_loot():
    # arguments: belt, health_points
    print("    | Test 1 for use loot")
    # Test belt with an incorrect input
    use_loot([], 9)
    print("    | Test 2 for use loot")
    # Test health_points with an incorrect input
    use_loot(["Leather Boots", "Secret Note"], -2)


# Lab 6 Answer 1 - Test the Collect Loot Function
def test_collect_loot():
    # Arguments are loot_options, belt
    print("    | Test 1 collect_loot()")
    # Test with incorrect argument for loot_options
    collect_loot([], [])
    print("    | Test 2 collect_loot()")
    # Test with incorrect argument for belt. Belt contains 6 items
    collect_loot(["Health Potion", "Flimsy Gloves"],
                 ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves",
                  "Flying Underpants"])


# Lab 6 Answer 2 - Test the Hero Attacks Function
def test_hero_attacks():
    # Arguments are combat_strength, m_health_points
    print("    | Test 1 hero_attacks()")
    # Test with incorrect argument for combat_strength
    hero_attacks(0, 13)
    print("    | Test 2 hero_attacks()")
    # Test with incorrect argument for m_health_points
    hero_attacks(7, -1)


# Lab 6 Answer 3 - Test the Monster Attacks Function
def test_monster_attacks():
    # Arguments are m_combat_strength, health_points
    print("    | Test 1 monster_attacks()")
    # Test with incorrect argument for m_combat_strength
    monster_attacks(-5, 6)
    print("    | Test 2 monster_attacks()")
    # Test with incorrect argument for health_points
    monster_attacks(5, 0)


# Lab 6 Answer 4 - Test the Final Score Function
def test_final_score():
    print("    | Test 1 final_score()")
    final_score(-1)
    print("    | Test 2 final_score()")
    final_score(15)
