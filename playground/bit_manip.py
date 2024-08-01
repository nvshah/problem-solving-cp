def find_lsb_position(num):
    '''lsb is first set bit from right side in a number's binary repr
    '''
    if num == 0:
        return "No LSB in zero"
    
    # Get the and operation between number & two's complement of the number 
    #   => result in a number that will hold MSB = 1 & rest 0
    two_complement = num & -num
    
    # Calculate the position of the rightmost set bit
    position = 0
    while two_complement != 1:
        two_complement >>= 1
        position += 1
        
    return position