#!/usr/bin/python3
'''Lockboxes Algorithm problem'''


def canUnlockAll(boxes):
    '''Solution function'''
    if not boxes:
        return False
    count = len(boxes)
    visited = [False] * count
    stack = [0]
    visited[0] = True
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < count and visited[key] is False:
                visited[key] = True
                stack.append(key)
    return all(visited)
