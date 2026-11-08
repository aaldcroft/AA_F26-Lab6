# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcrft 
# Date:11-07-26
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

## lab6c.py
### Set Operations


# TO DO 1: Copy the code from lab5b.py and paste here.
# TO DO 2: Create the function s3_and_s5_not_s7().
# TO DO 3: Run the script. Take screenshot of only s3_and_s5_not_s7() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.


def buildtheSet(divisor):
    numbers = set()  
    for i in range(0,101):
        if i % divisor == 0:
            numbers.add(i)
    return numbers
   
def s3_or_s5(s3,s5):
   
    combined = s3.union(s5)
    common = s3.intersection(s5)
    result = combined.difference(common)
    return result

def s3_and_s5_not_s7(s3,s5,s7):
    s3ands5 = s3.intersection(s5)
    s7common = s3ands5.intersection(s7)
    notin7 = s3ands5.difference(s7common)
    return notin7

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s3ands5nots7 = s3_and_s5_not_s7(s3,s5,s7)
    print("s3 and s5 not s7: ",s3ands5nots7)
    print("----------------------------------------")


main()
