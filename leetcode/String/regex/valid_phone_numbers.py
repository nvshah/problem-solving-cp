# https://leetcode.com/problems/valid-phone-numbers/

import re

# Patter that identifies :-
# (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
regex = r"^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$"

with open('leetcode/String/regex/valid_phone_numbers_file.txt', 'r') as f:
    pattern = re.compile(regex)
    for line in f:
        if pattern.match(line):
            print(line)

