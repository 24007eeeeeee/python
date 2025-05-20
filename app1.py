# docstring- Chris Wong- Star Wars database application
# imports
import sqlite3

# contants and variables
DATABASE = "SWfilms.db"


# functions
def print_all_movie():
    '''print all the movies nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from movie;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("|movie_name                   |director_id |duration_in_minutes |rating |box_office ")
    for movie in results:
        print(f"|{movie[1]:<30}{movie[2]:<13}{movie[3]:<21}{movie[4]:<8}{movie[5]:<25}")
    # loop finished here
    db.close

def print_all_movie_by_duration():
    '''print all the movies sorted by duration'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM movie ORDER BY duration_in_minutes; DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("|movie_name                   |director_id |duration_in_minutes |rating |box_office ")
    for movie in results:
        print(f"|{movie[1]:<30}{movie[2]:<13}{movie[3]:<21}{movie[4]:<8}{movie[5]:<25}")
    #loop finished here
    db.close


# main code
while True:
    user_input = input(
"""
What would you like to do.
1. Print all movies
2. Print all movies sorted by duration
3. Print all movies sorted by box_office
7. Exit
""")
    if user_input == "1":
        print_all_movie()
    elif user_input == "2":
        print_all_movie_by_duration
        




while True:
    user_input = input("\nWhat would you like to do.\n1. Print all movies.\n2. Sort movie order by duration\n3. Sort movie order by Box_office")
    if user_input == "1":
        print_all_movie()
    elif user_input == "2":
        print_all_movie_by_duration
