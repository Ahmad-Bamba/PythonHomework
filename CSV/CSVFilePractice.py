# CSV File Practice
# Ahmad Bamba
# 11/29/2016

import sys

class Film:
    def __init__(self, row):
        self.year = row[0]
        self.name = row[1]
        self.genre = row[2].replace(" ", "")

    def getYear(self):
        return self.year
    def getName(self):
        return self.name
    def getGenre(self):
        return self.genre

valid_genres = [ 'action', 'adventure', 'biopic', 'comedy', 'crime', 'drama', 'epic',
                 'fantasy', 'musical', 'silent', 'sports', 'romance', 'thriller', 'war', 'western' ]

_file = open("Academy Awards Best Picture Year and Genre.txt", 'r')
raw = _file.read()
_file.close()

lines = raw.splitlines()
formatted = [line.split(",") for line in lines]
movies = []

for thing in formatted:
    movies.append(Film(thing))

while True:
    user = raw_input("\nEnter genre(q to quit): ")
    if user.lower() == "q":
        "Exiting on user request"
        sys.exit()
    if user.lower() not in valid_genres:
        print "Not a valid genre"
    else:
        matches = []
        for movie in movies:
            if movie.getGenre().lower() == user.lower():
                matches.append(movie)
        print "The award winners are: "
        for movie in matches:
            print "Movie: " + movie.getName() + " Year: " + movie.getYear()
