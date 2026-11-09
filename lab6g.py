# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcrft 
# Date:11-07-26
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

movie_list = []
def add_movies(name,director,year,runtime):
   movie= {
      "name":name,
      "director":director,
      "year":year,
      "runtime":runtime}
   movie_list.append(movie)
   
def main():
      add_movies("Incantation","Kevin Ko","2022","1h50m")
      add_movies("Internal Sunshine of the Spotless Mind","Michel Gondry","2004","1h48m")
      add_movies("Girl, Interrupted","James Mangold","1999","2h7m")
      print(movie_list)

main()   