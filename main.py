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
print("2. Exit")

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
    print("You selected:", genre)

elif choice == "2":
    print()
    print("Thanks for using Album Discovery Generator!")

else:
    print()
    print("Invalid choice.")