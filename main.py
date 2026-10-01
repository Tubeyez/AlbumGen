import random

albums = [
    {
        "title": "Thriller",
        "artist": "Michael Jackson",
        "genre": "Pop",
        "mood": "Energetic",
        "year": 1982
    },
    {
        "title": "1989",
        "artist": "Taylor Swift",
        "genre": "Pop",
        "mood": "Happy",
        "year": 2014
    },
    {
        "title": "Nevermind",
        "artist": "Nirvana",
        "genre": "Rock",
        "mood": "Energetic",
        "year": 1991
    },
    {
        "title": "AM",
        "artist": "Arctic Monkeys",
        "genre": "Rock",
        "mood": "Chill",
        "year": 2013
    },
    {
        "title": "DAMN.",
        "artist": "Kendrick Lamar",
        "genre": "Hip-Hop",
        "mood": "Energetic",
        "year": 2017
    },
    {
        "title": "Flower Boy",
        "artist": "Tyler, The Creator",
        "genre": "Hip-Hop",
        "mood": "Chill",
        "year": 2017
    },
    {
        "title": "Blonde",
        "artist": "Frank Ocean",
        "genre": "R&B",
        "mood": "Chill",
        "year": 2016
    },
    {
        "title": "SOS",
        "artist": "SZA",
        "genre": "R&B",
        "mood": "Sad",
        "year": 2022
    },
    {
        "title": "Random Access Memories",
        "artist": "Daft Punk",
        "genre": "Electronic",
        "mood": "Energetic",
        "year": 2013
    },
    {
        "title": "Discovery",
        "artist": "Daft Punk",
        "genre": "Electronic",
        "mood": "Happy",
        "year": 2001
    },
    {
        "title": "Currents",
        "artist": "Tame Impala",
        "genre": "Alternative",
        "mood": "Chill",
        "year": 2015
    },
    {
        "title": "The New Abnormal",
        "artist": "The Strokes",
        "genre": "Alternative",
        "mood": "Chill",
        "year": 2020
    }
]

print("======================================")
print("       ALBUM DISCOVERY GENERATOR")
print("======================================")

print()
print("Discover albums based on your music preferences.")
print()

print("1. Find an album")
print("2. Surprise me")
print("3. Exit")


choice = input("Enter your choice: ")

if choice == "1":
    print()
    print("Choose your preferred genre:")
    print("1. Pop")
    print("2. Rock")
    print("3. Hip-Hop")
    print("4. R&B")
    print("5. Electronic")
    print("6. Alternative")

    genre_choice = input("Enter your choice: ")

    if genre_choice == "1":
        genre = "Pop"
    elif genre_choice == "2":
        genre = "Rock"
    elif genre_choice == "3":
        genre = "Hip-Hop"
    elif genre_choice == "4":
        genre = "R&B"
    elif genre_choice == "5":
        genre = "Electronic"
    elif genre_choice == "6":
        genre = "Alternative"
    else:
        genre = "Unknown"

    print()
    print("Choose your preferred mood:")
    print("1. Chill")
    print("2. Energetic")
    print("3. Happy")
    print("4. Sad")

    mood_choice = input("Enter your choice: ")

    if mood_choice == "1":
        mood = "Chill"
    elif mood_choice == "2":
        mood = "Energetic"
    elif mood_choice == "3":
        mood = "Happy"
    elif mood_choice == "4":
        mood = "Sad"
    else:
        mood = "Unknown"

    matching_albums = []

    for album in albums:
        if album["genre"] == genre and album["mood"] == mood:
            matching_albums.append(album)

    print()
    print("Albums matching your genre:")

    for album in matching_albums:
        print(album["title"], "-", album["artist"])

    print()
    print("You selected:")
    print("Genre:", genre)
    print("Mood:", mood)

    if len(matching_albums) > 0:
        print()
        print("Albums matching your preferences:")

        for album in matching_albums:
            print(album["title"], "-", album["artist"])

    else:
        print()
        print("No albums found matching your preferences.")


elif choice == "2":
    """Pick one random album from the whole list."""
    album = random.choice(albums)
    print()
    print("Surprise! Try this album:")
    print("Title :", album["title"])
    print("Artist:", album["artist"])
    print("Genre :", album["genre"])
    print("Mood  :", album["mood"])
    print("Year  :", album["year"])

elif choice == "3":
    print()
    print("Thanks for using Album Discovery Generator!")

else:
    print()
    print("Invalid choice.")