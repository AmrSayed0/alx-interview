#!/usr/bin/python3
"""Solution to Lockboxes problem"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list): A list of lists containing keys to other boxes.
    
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for k in range(1, len(boxes) - 1):
        unlocked = False
        for i in range(len(boxes)):
            unlocked = k in boxes[i] and k != i
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True
