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
    for movie in results:
        print(movie)
    # loop finished here
    db.close

# main code
print_all_movie()

