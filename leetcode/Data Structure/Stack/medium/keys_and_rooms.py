# https://leetcode.com/problems/keys-and-rooms/description/

'''
As we need to follow a sequence in Visit
because We are only allowed to enter first room
Now lateral visit will be define based on key availability
So we can use Stack Data Structure here (as there is a sequence/pipeline needs to be followed)

'''

def canVisitAllRooms(rooms):
    # left := rooms yet to be explored
    # stack := current rooms that can be explored
    unexplored, stack = set(range(len(rooms))), [0]
    while stack: 
        # Visit the next room
        toVisit = stack.pop()
        unexplored.discard(toVisit)  # Remove it from unexplored list
        for room in rooms[toVisit]:
            # If this room is not yet visited
            if room in unexplored:
                stack.append(room)  # make it in pipeline

    return not unexplored  # No rooms left being unexplored (ie all ar explored)