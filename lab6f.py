# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcrft 
# Date:11-07-26
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

# TO DO 1: Create function histogram() as instructed in readme.md file. 
# TO DO 2: Create main() function and call histogram(). Call the main() function.
# TO DO 3: Run the script. Take screenshot of code showing the functions histogram() and main(). Also show output in the screenshot.

def histogram(text):
    letter_counts = {}
    for letters in text:
        if letters == " ":
            continue
        if letters in letter_counts:
            letter_counts[letters] = letter_counts[letters] + 1
        else:
            letter_counts[letters] = 1
    
    for letters in letter_counts:
        print(letters,"*" * letter_counts[letters])

histogram("hello my name is abby")
