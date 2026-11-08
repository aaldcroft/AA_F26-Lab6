# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Abby Aldcroft  
# Date:11-07-26
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py
# TO DO 1: Copy the code from lab6a.py and paste here.
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
    

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s3ors5 = s3_or_s5(s3,s5)
    print("s3 or s5",s3ors5)

main()

# TO DO 2: Create the function s3ors5().





# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
