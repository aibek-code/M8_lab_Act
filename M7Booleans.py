# Write a function 
import resources

def check_items(number):
    print("this isn't working right now!")
    print(f"{resources.aibek.weapons}")
    if number == 1:
        # for every item on the list that I need, I want to see if it is in my weapons

        required_items = ['rope', 'coat', 'first aid kit']
        for item in required_items:
            if item not in resources.aibek.weapons:
                print(f"Hey, you don't have {item}")
                return False
            
        if 'slow' in resources.aibek.weaknesses:
            print("You cannot climb a mountain because you're too slow.")
            return False
        
        print("You have everything you need to climb the mountain!")
        return True
        
    elif number == 2:
        required_items = ['pan', 'groceries']
        print(f"Required items: {required_items}")

        for item in required_items:
            if item not in resources.aibek.weapons:
                print(f"Hey, you don't have {item}")
                return False

        if 'small' in resources.aibek.weaknesses:
            print("You cannot cook a meal because you're too small.")
            return False
        
        print("You have everything you need to cook a meal!")
        return True


    elif number == 3:
        required_items = ['pen', 'paper', 'idea']
        print(f"Required items: {required_items}")
    #the number has to connect to a specific list
    #print out the list connected to the task number
    #if the number is 1, print out ["pan","coat","first iad kit"]
    #if the number is 2, print out ["pan","groceries"]
        for item in required_items:
            if item not in resources.aibek.weapons:
                print(f"Hey, you don't have {item}")
                return False
            
        if 'confusion' in resources.aibek.weaknesses:
            print("You cannot write a book because you're too confused.")
            return False
        
        print("You have everything you need to write a book!")
        return True

    else:
        print("Invalid task number. Please choose a task number between 1 and 3.")
        return False



check_items(1)
check_items(2)
check_items(3)
# see printed out: ["pan", "groceries"]

# (in M7Booleans.py) that checks whether your game character has
# picked up all the items needed to perform certain tasks and checks against any weaknesses.
# Confirm checks with print statements. The function will take a number in as an argument. You
# can match the number to the task below. You don’t have to plan for inputs outside of [1,2,3].

# how do I look in my character weapon



