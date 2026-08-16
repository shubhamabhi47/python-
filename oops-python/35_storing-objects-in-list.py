# ============================================================
# OOP PROJECT: MOVIE MANAGEMENT USING OBJECTS + LIST
# ============================================================
# A list can store multiple objects of the same class.
# This is useful when working with collections of real-world
# entities such as movies, students, employees, products, etc.
#
# Instead of creating:
#     m1, m2, m3, m4...
#
# we can dynamically create objects and store them in:
#     movies = []
#
# Each object keeps its own state while the class defines the
# common structure and behavior.
# ============================================================


# ============================================================
# 1. MOVIE CLASS
# ============================================================
class Movie:
    def __init__(self, title, runtime, hero):
        self.title = title
        self.runtime = runtime
        self.hero = hero

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Runtime: {self.runtime} minutes")
        print(f"Hero: {self.hero}")


# ============================================================
# 2. CREATING AND STORING OBJECTS
# ============================================================
movies = []

m1 = Movie("Inception", 148, "Leonardo DiCaprio")
m2 = Movie("Interstellar", 169, "Matthew McConaughey")

movies.append(m1)
movies.append(m2)


# ============================================================
# 3. ITERATING THROUGH OBJECTS
# ============================================================
for movie in movies:
    movie.display_info()
    print("-" * 30)


# ============================================================
# 4. DIRECT OBJECT CREATION + APPEND
# ============================================================
movies.append(Movie("The Dark Knight", 152, "Christian Bale"))

for movie in movies:
    print(movie.title)


# ============================================================
# 5. USER INPUT
# ============================================================
# input() always returns a string, so runtime should be
# converted to int before creating the object.

while True:
    title = input("Enter movie title: ").strip()
    runtime = int(input("Enter runtime in minutes: "))
    hero = input("Enter hero name: ").strip()

    movies.append(Movie(title, runtime, hero))

    choice = input("Add another movie? (yes/no): ").strip().lower()

    if choice != "yes":
        break


# ============================================================
# 6. DISPLAY ALL MOVIES
# ============================================================
for movie in movies:
    movie.display_info()
    print("-" * 30)


# ============================================================
# 7. BETTER VERSION: __str__
# ============================================================
# Instead of manually printing every attribute, __str__()
# provides a readable representation of an object.

class Movie:
    def __init__(self, title, runtime, hero):
        self.title = title
        self.runtime = runtime
        self.hero = hero

    def __str__(self):
        return f"{self.title} | {self.runtime} min | {self.hero}"


movies = [
    Movie("Inception", 148, "Leonardo DiCaprio"),
    Movie("Interstellar", 169, "Matthew McConaughey"),
    Movie("The Dark Knight", 152, "Christian Bale")
]

for movie in movies:
    print(movie)


# ============================================================
# 8. ADDING SEARCH FUNCTIONALITY
# ============================================================
class Movie:
    def __init__(self, title, runtime, hero):
        self.title = title
        self.runtime = runtime
        self.hero = hero

    def __str__(self):
        return f"{self.title} | {self.runtime} min | {self.hero}"


movies = [
    Movie("Inception", 148, "Leonardo DiCaprio"),
    Movie("Interstellar", 169, "Matthew McConaughey"),
    Movie("The Dark Knight", 152, "Christian Bale")
]


def search_movie(movies, title):
    for movie in movies:
        if movie.title.casefold() == title.casefold():
            return movie
    return None


result = search_movie(movies, "inception")

if result:
    print(result)
else:
    print("Movie not found")


# ============================================================
# 9. FILTERING MOVIES
# ============================================================
# List comprehensions make it easy to filter objects based on
# their attributes.

long_movies = [movie for movie in movies if movie.runtime > 150]

for movie in long_movies:
    print(movie)


# ============================================================
# 10. FINDING THE LONGEST MOVIE
# ============================================================
longest = max(movies, key=lambda movie: movie.runtime)

print("Longest movie:", longest)


# ============================================================
# 11. SORTING OBJECTS
# ============================================================
# Objects can be sorted according to any attribute.

movies.sort(key=lambda movie: movie.title)

for movie in movies:
    print(movie)


# Sort by runtime from longest to shortest
movies.sort(key=lambda movie: movie.runtime, reverse=True)

for movie in movies:
    print(movie)


# ============================================================
# 12. DELETING A MOVIE
# ============================================================
def delete_movie(movies, title):
    for i, movie in enumerate(movies):
        if movie.title.casefold() == title.casefold():
            del movies[i]
            return True
    return False


delete_movie(movies, "Inception")

for movie in movies:
    print(movie)


# ============================================================
# 13. BETTER DESIGN: MOVIE COLLECTION CLASS
# ============================================================
# Once the program becomes larger, it is cleaner to separate:
#
#     Movie        -> represents one movie
#     MovieLibrary -> manages multiple movies
#
# This follows the Single Responsibility Principle more closely.

class Movie:
    def __init__(self, title, runtime, hero):
        self.title = title
        self.runtime = runtime
        self.hero = hero

    def __str__(self):
        return f"{self.title} | {self.runtime} min | {self.hero}"


class MovieLibrary:
    def __init__(self):
        self.movies = []

    def add(self, movie):
        self.movies.append(movie)

    def display_all(self):
        for movie in self.movies:
            print(movie)

    def search(self, title):
        return next(
            (movie for movie in self.movies
             if movie.title.casefold() == title.casefold()),
            None
        )

    def delete(self, title):
        movie = self.search(title)

        if movie:
            self.movies.remove(movie)
            return True

        return False

    def sort_by_runtime(self, reverse=False):
        self.movies.sort(
            key=lambda movie: movie.runtime,
            reverse=reverse
        )


library = MovieLibrary()

library.add(Movie("Inception", 148, "Leonardo DiCaprio"))
library.add(Movie("Interstellar", 169, "Matthew McConaughey"))
library.add(Movie("The Dark Knight", 152, "Christian Bale"))

library.display_all()

print("Search:", library.search("Interstellar"))

library.sort_by_runtime(reverse=True)
library.display_all()


# ============================================================
# 14. USER-DRIVEN MOVIE LIBRARY
# ============================================================
class Movie:
    def __init__(self, title, runtime, hero):
        self.title = title
        self.runtime = runtime
        self.hero = hero

    def __str__(self):
        return f"{self.title} | {self.runtime} min | {self.hero}"


class MovieLibrary:
    def __init__(self):
        self.movies = []

    def add_movie(self):
        title = input("Title: ").strip()
        runtime = int(input("Runtime: "))
        hero = input("Hero: ").strip()

        self.movies.append(Movie(title, runtime, hero))

    def display_all(self):
        if not self.movies:
            print("No movies available")
            return

        for movie in self.movies:
            print(movie)

    def search(self):
        title = input("Search title: ").strip()

        for movie in self.movies:
            if movie.title.casefold() == title.casefold():
                print(movie)
                return

        print("Movie not found")


library = MovieLibrary()

while True:
    print("\n1. Add Movie")
    print("2. Display Movies")
    print("3. Search Movie")
    print("4. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        library.add_movie()
    elif choice == "2":
        library.display_all()
    elif choice == "3":
        library.search()
    elif choice == "4":
        break
    else:
        print("Invalid choice")


# ============================================================
# 15. ADVANCED: DATACLASS VERSION
# ============================================================
# For classes that mainly store data, dataclasses can reduce
# boilerplate such as __init__ and __repr__.

from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    runtime: int
    hero: str


movies = [
    Movie("Inception", 148, "Leonardo DiCaprio"),
    Movie("Interstellar", 169, "Matthew McConaughey")
]

for movie in movies:
    print(movie)


# ============================================================
# 16. ADVANCED: VALIDATION
# ============================================================
# Objects should ideally reject invalid state at creation time.

class Movie:
    def __init__(self, title, runtime, hero):
        title = title.strip()
        hero = hero.strip()

        if not title:
            raise ValueError("Title cannot be empty")

        if runtime <= 0:
            raise ValueError("Runtime must be positive")

        if not hero:
            raise ValueError("Hero name cannot be empty")

        self.title = title
        self.runtime = runtime
        self.hero = hero

    def __str__(self):
        return f"{self.title} | {self.runtime} min | {self.hero}"


movie = Movie("Inception", 148, "Leonardo DiCaprio")
print(movie)


# ============================================================
# KEY CONCEPT
# ============================================================
# A list of objects gives us a simple in-memory collection:
#
#     movies = [
#         Movie(...),
#         Movie(...),
#         Movie(...)
#     ]
#
# Each element is an independent object.
#
#     movies[0].title
#     movies[1].title
#
# accesses different objects.
#
# The major OOP idea here is:
#
#     CLASS  -> defines structure + behavior
#     OBJECT -> represents one movie
#     LIST   -> stores many movie objects
#
# As the application grows, separating Movie from
# MovieLibrary makes the design cleaner and easier to extend.
# ============================================================