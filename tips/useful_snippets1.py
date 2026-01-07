# Create a dictionary that maps numbers 1 to 26 to letters 'a' to 'z'
number_to_letter = {i: chr(96 + i) for i in range(1, 27)}

# Create a dictionary that maps letters 'a' to 'z' to numbers 1 to 26
letter_to_number = {chr(96 + i): i for i in range(1, 27)}


# Create a list of letters from 'a' to 'z'
letters = [chr(i) for i in range(97, 123)]
