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

# main code
print_all_movie()