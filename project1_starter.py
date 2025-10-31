"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kenneth Tyler
Date: 10/30/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os
# Character system config

class_modifiers = {
    "Warrior": {"strength": 12, "magic": 3, "health": 150},
    "Mage": {"strength": 2, "magic": 15, "health": 110},
    "Rogue": {"strength": 6, "magic": 7, "health": 125},
    "Cleric": {"strength": 6, "magic": 10, "health": 167}
}

# Main functions

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    if character_class not in class_modifiers:
        print(f"Error: {character_class} is not a valid class")
        return None

    level = 1
    gold = 100
    calcs = calculate_stats(character_class, level)
    strength = calcs[0]
    magic = calcs[1]
    health = calcs[2]
    # Checks if class is one of the class modifiers
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

    # This function returns 0 for strength, magic, and health
    if character_class not in class_modifiers:
        return 0, 0, 0

    base_stat = class_modifiers[character_class]
    strength = base_stat["strength"] + (level * 2)
    magic = base_stat["magic"] + (level * 3)
    health = base_stat["health"] + (level * 10)
    stats = strength, magic, health
    return stats

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    # Split path to get directory
    path_parts = os.path.split(filename)
    directory = path_parts[0]  # folder path
    file_name = path_parts[1]  # file name

    # Default to current directory if empty
    if directory == "":
        directory = "."

    # Check if directory exists; if not, can't save
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return False

    # Construct full path (in case directory was provided)
    full_path = os.path.join(directory, file_name)

    # Open file and write character data
    f = open(full_path, "w")
    f.write(f"Character Name: {character['name']}\n")
    f.write(f"Class: {character['class']}\n")
    f.write(f"Level: {character['level']}\n")
    f.write(f"Strength: {character['strength']}\n")
    f.write(f"Magic: {character['magic']}\n")
    f.write(f"Health: {character['health']}\n")
    f.write(f"Gold: {character['gold']}\n")
    f.close()

    # Verify file was created
    if os.path.exists(full_path):
        return True
    else:
        return False
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    # Check if file exists first
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    # Ensure file has exactly 7 lines (basic validation)
    if len(lines) != 7:
        print(f"Error: File '{filename}' is corrupted or invalid format.")
        return None

    # Parse each line
    name = lines[0].strip().split(": ")[1]
    character_class = lines[1].strip().split(": ")[1]
    level = int(lines[2].strip().split(": ")[1])
    strength = int(lines[3].strip().split(": ")[1])
    magic = int(lines[4].strip().split(": ")[1])
    health = int(lines[5].strip().split(": ")[1])
    gold = int(lines[6].strip().split(": ")[1])

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("======================")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    character["level"] += 1
    # Store the tuple in one variable
    stats = calculate_stats(character["class"], character["level"])
    # Access each stat by its index
    strength = stats[0]
    magic = stats[1]
    health = stats[2]
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 100

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    char = create_character("Oswald", "Mage")
    display_character(char)
    level_up(char)
    save_character(char, "my_character.txt")
    loaded_hero = load_character("my_character.txt")
    display_character(loaded_hero)
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

