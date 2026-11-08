# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcrft 
# Date:11-07-26
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

# TO DO 1: Create function times_ten as instructed in readme.md file. 

# TO DO 2: Run the script.
def times_ten(start_index: int, end_index: int):
    number_times_ten = {}

    for i in range(start_index,end_index + 1):
       
        multiple = i * 10
        number_times_ten[i] = multiple
    return number_times_ten

number_times_ten = times_ten(0,5)
print(number_times_ten)
