# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcrft 
# Date:11-07-26
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# TO DO 1: Copy the code from lab6g.py and paste here.
# TO DO 2: Create function find_movie().
# TO DO 3: Call the function as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.
movie_list = []
def add_movies(name,director,year,runtime):
   movie= {
      "name":name,
      "director":director,
      "year":year,
      "runtime":runtime}
   movie_list.append(movie)


def find_movie(movie_list, search_word):
    match=[]
    for movie in movie_list:
        if search_word.lower() in movie["name"].lower():
            match.append(movie)       
    return match

def main():
    add_movies("Incantation","Kevin Ko","2022","1h50m")
    add_movies("Internal Sunshine of the Spotless Mind","Michel Gondry","2004","1h48m")
    add_movies("Girl, Interrupted","James Mangold","1999","2h7m")
    add_movies("Catch Me if You Can","Steven Speilberg","2002","2h21m")
    
    
    result=find_movie(movie_list,"me")
    result2=find_movie(movie_list,"girl")
    
    all_results=result,result2,
    
    for movie in all_results:
        print("Search match: ",movie)
    

main()   

