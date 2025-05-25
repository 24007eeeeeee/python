# docstring- Chris Wong- Star Wars database application
# imports
import sqlite3

# contants and variables
DATABASE = "SWfilms.db"


# functions
def print_all_movie():
    '''print all the movies nicely'''
    # connects to the database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql query to select all from the movie table
    sql = "SELECT * from movie;"
    cursor.execute(sql)
    # fetches all results
    results = cursor.fetchall()
    # loop through all the results
    print("|movie_name                   |director_name |duration_in_minutes |rating |box_office ")
    # prints table headings in a formatted way
    for movie in results:
        print(f"|{movie[1]:<30}{movie[2]:<13}{movie[3]:<21}{movie[4]:<8}{movie[5]:<25}")
    # loop finished here
    db.close


def print_all_movie_by_duration():
    '''print all the movies sorted by duration'''
    # connects to the database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql query to select from movie in the order of duration_in_minutes
    sql = "SELECT * FROM movie ORDER BY duration_in_minutes DESC;"
    cursor.execute(sql)
    # fetches all results
    results = cursor.fetchall()
    # loop through all the results
    print("|movie_name                   |director_name |duration_in_minutes |rating |box_office ")
    # prints table headings in a formatted way
    for movie in results:
        print(f"|{movie[1]:<30}{movie[2]:<13}{movie[3]:<21}{movie[4]:<8}{movie[5]:<25}")
    # loop finished here
    db.close


def print_all_movie_sorted_by_box_office():
    '''print all the movies sorted by box office'''
    # connects to the database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # sql query to select from movie in the order of box_office
    sql = " SELECT * FROM movie ORDER BY box_office;"
    cursor.execute(sql)
    # fetches all results
    results = cursor.fetchall()
    # loop through all the results
    print("|movie_name                   |director_name |duration_in_minutes |rating |box_office ")
    # prints table headings in a formatted way
    for movie in results:
        print(f"|{movie[1]:<30}{movie[2]:<13}{movie[3]:<21}{movie[4]:<8}{movie[5]:<25}")
    # loop finished here
    db.close


# main code
while True:
    user_input = input(
"""
What would you like to do.
1. Print all movies
2. Print all movies sorted by duration
3. Print all movies sorted by box office
4. Exit
""")
    if user_input == "1":
        print_all_movie()
    elif user_input == "2":
        print_all_movie_by_duration()
    elif user_input == "3":
        print_all_movie_sorted_by_box_office()
    elif user_input == "4":
        # exit the loop and exits
        break
    # if user input not listed above then prints its not an option
    else:
        print("That was not an option\n")