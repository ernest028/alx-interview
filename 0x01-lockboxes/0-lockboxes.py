#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""
from collections import deque
def canUnlockAll(boxes):
    """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    and the other to compaer if key is idx or not in order to open
    """

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    queue = deque([0])

    while queue:
        curr_box = queue.popleft()
        for key in boxes[curr_box]:
            if key >= 0 and key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
