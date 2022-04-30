# https://leetcode.com/problems/robot-bounded-in-circle/

def isRobotBounded(instructions: str) -> bool:
    # NOTE :- for direction we'll use basis vectors ie
    #         (0,1) -> North
    #         (1,0) -> East
    #         (0, -1) -> South
    #         (-1, 0) -> West

    x = y = 0    # initially standinng at origin
    dirX, dirY = 0, 1  # Initially at origin & facing in North Direction

    for i in instructions:
        match i:
            case 'G':  # Go ahead
                x, y = x+dirX, y+dirY
            case 'L':  # Turn left
                dirX, dirY = -dirY, dirX  
            case 'R':  # Turn right
                dirX, dirY = dirY, -dirX

    # After executing all instructions once, if 
    # 1) We came to same place from where started (ie origin) then its loop
    # 2) We change direction from initial direction (ie North Facing) then also its gonna loop eventually later (ie after 0, 2 or 4 steps)

    return (x,y) == (0,0) or (dirX, dirY) != (0, 1)