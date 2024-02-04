import random

def roll_dice(num_rolls, num_faces):
    """
    Simulate rolling a dice.

    Parameters:
    num_rolls (int): Number of times to roll the dice.
    num_faces (int): Number of faces on the dice.

    Returns:
    list: A list containing the results of each roll.
    """
    results = []
    for _ in range(num_rolls):
        roll_result = random.randint(1, num_faces)
        results.append(roll_result)
    return results

# example
num_rolls = 5  
num_faces = 6  

rolls = roll_dice(num_rolls, num_faces)
print("Results of rolling the dice:", rolls)
