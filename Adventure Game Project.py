import random

enemy_name_list = ["enemy tanks", "enemy soldiers", "zombies", "Mountain lions"]
enemy_intro_list = ["Heavy shadows quickly approaching!", "There's something in the woods!", "A blind sided attack!", "What's that noise approaching?!"]

#Class
class Rambo:
    
    def __init__(self, name, supply_drops, life_points):
        self.name = name
        self.Miles_Traveled = 0
        self.supply_drops = supply_drops
        self.life_points = life_points
    
    def __str__(self):
        ret = "***Across Enemy Lines***\n"
        ret += "Soldier: " + self.name + "\n"
        ret += "Miles Traveled: " + str(self.Miles_Traveled) + "\n"
        ret += "Supply Drops: " + str(self.supply_drops) + "\n"
        ret += "Life Points: " + str(self.life_points) + "\n"
        ret += "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
        return ret

# Enemy
class Enemy:
    
    def __init__(self, name, Miles_Traveled, introduction, damage):
        self.name = name
        self.Miles_Traveled = Miles_Traveled
        self.introduction = introduction
        self.damage = damage
    def __str__(self):
        ret = "Across Enemy Lines\n"
        ret += "Enemy: " + self.name + "\n"
        ret += "Miles_Traveled: " + str(self.Miles_Traveled)
        ret += "Introduction: " + str(self.introduction) + "\n"
        ret += "Damage: " + str(self.damage) + "\n"
        ret += "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
        return ret

#loop
def play(rambo, enemies, path_length):
    print("You are Billy Brooks, an Army Soldier caught in the middle of the next World War.")
    print("Your job is to make it up and across the war hill arriving safely to an ally military base.")
    print("You have a 100 Life Points.")
    print("Anything lower than 0 puts you in critical condition and you failed the mission.")
    print("Beware of enemy tanks, enemy soldiers, zombies, and mountain lions.") 
    print("Mission Accepted:")
    for i in range(1, path_length+1): # Loop path
        input("\nPress Enter to move forward.\n") 
        rambo.Miles_Traveled = i 
        print(rambo.name + " traveled " + str(rambo.Miles_Traveled), "mile.")
        for enemy in enemies:
            if rambo.Miles_Traveled == enemy.Miles_Traveled: 
                rambo.life_points -= enemy.damage 
                print(random.choice(enemy_intro_list))
                print("You were attacked by " + enemy.name + " and lost " + str(enemy.damage) + " Life Points.")
                break
        else: # Enemy encounter
            pickup = random.randint(5,10 )
            rambo.supply_drops += pickup
            print("You recieved " + str(pickup) + " supply drops.")
        if rambo.life_points <= 0: #Failed mission
            print("\n\n" + rambo.name + " remains in critical condition and failed the mission....")
            break
    else:
        print(" ")
        print(" ")
        print("Congratulations and Well Done! ")
        print(rambo.name + " completed the mission and arrived to base safely!") #Mission Complete

# Start the game
def main():
    path_length = 10
    rambo = Rambo("Billy Brooks", 0, 100)
    num_enemies = random.randint(int(0.3*path_length), int(0.7*path_length)) # 30%-70% steps will have enemies
    enemies = []
    for _ in range(num_enemies):
        enemy_name, enemy_intro = random.choice(enemy_name_list), random.choice(enemy_intro_list)
        enemy_Miles_Traveled, enemy_damage = random.randint(1, path_length), random.randint(10, 35)
        enemies.append(Enemy(enemy_name, enemy_Miles_Traveled, "It's " + enemy_name + enemy_intro, enemy_damage))
    play(rambo, enemies, path_length) # Play the game
    print("\n\nEnd of the game results:") # Print the results
    print(rambo)

if __name__ == "__main__":
    main()