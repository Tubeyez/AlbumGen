import random
import webbrowser
from urllib.parse import quote_plus
# ---------- DATA: full albums (every genre + mood combo has one) ----------
albums = [
    # Pop
    {"title": "folklore", "artist": "Taylor Swift", "genre": "Pop", "mood": "Chill", "year": 2020},
    {"title": "Thriller", "artist": "Michael Jackson", "genre": "Pop", "mood": "Energetic", "year": 1982},
    {"title": "Future Nostalgia", "artist": "Dua Lipa", "genre": "Pop", "mood": "Energetic", "year": 2020},
    {"title": "1989", "artist": "Taylor Swift", "genre": "Pop", "mood": "Happy", "year": 2014},
    {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "mood": "Happy", "year": 2019},
    {"title": "Happier Than Ever", "artist": "Billie Eilish", "genre": "Pop", "mood": "Sad", "year": 2021},
    # Rock
    {"title": "AM", "artist": "Arctic Monkeys", "genre": "Rock", "mood": "Chill", "year": 2013},
    {"title": "Rumours", "artist": "Fleetwood Mac", "genre": "Rock", "mood": "Chill", "year": 1977},
    {"title": "Nevermind", "artist": "Nirvana", "genre": "Rock", "mood": "Energetic", "year": 1991},
    {"title": "Abbey Road", "artist": "The Beatles", "genre": "Rock", "mood": "Happy", "year": 1969},
    {"title": "Wish You Were Here", "artist": "Pink Floyd", "genre": "Rock", "mood": "Sad", "year": 1975},
    # Hip-Hop
    {"title": "Flower Boy", "artist": "Tyler, The Creator", "genre": "Hip-Hop", "mood": "Chill", "year": 2017},
    {"title": "DAMN.", "artist": "Kendrick Lamar", "genre": "Hip-Hop", "mood": "Energetic", "year": 2017},
    {"title": "Graduation", "artist": "Kanye West", "genre": "Hip-Hop", "mood": "Happy", "year": 2007},
    {"title": "Mr. Morale & the Big Steppers", "artist": "Kendrick Lamar", "genre": "Hip-Hop", "mood": "Sad", "year": 2022},
    # R&B
    {"title": "Blonde", "artist": "Frank Ocean", "genre": "R&B", "mood": "Chill", "year": 2016},
    {"title": "Confessions", "artist": "Usher", "genre": "R&B", "mood": "Energetic", "year": 2004},
    {"title": "Songs in the Key of Life", "artist": "Stevie Wonder", "genre": "R&B", "mood": "Happy", "year": 1976},
    {"title": "SOS", "artist": "SZA", "genre": "R&B", "mood": "Sad", "year": 2022},
    # Electronic
    {"title": "Selected Ambient Works 85-92", "artist": "Aphex Twin", "genre": "Electronic", "mood": "Chill", "year": 1992},
    {"title": "Random Access Memories", "artist": "Daft Punk", "genre": "Electronic", "mood": "Energetic", "year": 2013},
    {"title": "Discovery", "artist": "Daft Punk", "genre": "Electronic", "mood": "Happy", "year": 2001},
    {"title": "Untrue", "artist": "Burial", "genre": "Electronic", "mood": "Sad", "year": 2007},
    # Alternative
    {"title": "Currents", "artist": "Tame Impala", "genre": "Alternative", "mood": "Chill", "year": 2015},
    {"title": "The New Abnormal", "artist": "The Strokes", "genre": "Alternative", "mood": "Chill", "year": 2020},
    {"title": "Is This It", "artist": "The Strokes", "genre": "Alternative", "mood": "Energetic", "year": 2001},
    {"title": "Torches", "artist": "Foster the People", "genre": "Alternative", "mood": "Happy", "year": 2011},
    {"title": "OK Computer", "artist": "Radiohead", "genre": "Alternative", "mood": "Sad", "year": 1997},
]

# ---------- DATA: single songs used by the album builder ----------
songs = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "mood": "Energetic", "year": 2019},
    {"title": "Levitating", "artist": "Dua Lipa", "genre": "Pop", "mood": "Happy", "year": 2020},
    {"title": "bad guy", "artist": "Billie Eilish", "genre": "Pop", "mood": "Chill", "year": 2019},
    {"title": "drivers license", "artist": "Olivia Rodrigo", "genre": "Pop", "mood": "Sad", "year": 2021},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "genre": "Rock", "mood": "Energetic", "year": 1991},
    {"title": "Here Comes the Sun", "artist": "The Beatles", "genre": "Rock", "mood": "Happy", "year": 1969},
    {"title": "Do I Wanna Know?", "artist": "Arctic Monkeys", "genre": "Rock", "mood": "Chill", "year": 2013},
    {"title": "Wish You Were Here", "artist": "Pink Floyd", "genre": "Rock", "mood": "Sad", "year": 1975},
    {"title": "HUMBLE.", "artist": "Kendrick Lamar", "genre": "Hip-Hop", "mood": "Energetic", "year": 2017},
    {"title": "Good Life", "artist": "Kanye West", "genre": "Hip-Hop", "mood": "Happy", "year": 2007},
    {"title": "See You Again", "artist": "Tyler, The Creator", "genre": "Hip-Hop", "mood": "Chill", "year": 2017},
    {"title": "Runaway", "artist": "Kanye West", "genre": "Hip-Hop", "mood": "Sad", "year": 2010},
    {"title": "Yeah!", "artist": "Usher", "genre": "R&B", "mood": "Energetic", "year": 2004},
    {"title": "Signed, Sealed, Delivered I'm Yours", "artist": "Stevie Wonder", "genre": "R&B", "mood": "Happy", "year": 1970},
    {"title": "Nights", "artist": "Frank Ocean", "genre": "R&B", "mood": "Chill", "year": 2016},
    {"title": "Kill Bill", "artist": "SZA", "genre": "R&B", "mood": "Sad", "year": 2022},
    {"title": "Harder, Better, Faster, Stronger", "artist": "Daft Punk", "genre": "Electronic", "mood": "Energetic", "year": 2001},
    {"title": "One More Time", "artist": "Daft Punk", "genre": "Electronic", "mood": "Happy", "year": 2000},
    {"title": "Porcelain", "artist": "Moby", "genre": "Electronic", "mood": "Chill", "year": 1999},
    {"title": "Archangel", "artist": "Burial", "genre": "Electronic", "mood": "Sad", "year": 2007},
    {"title": "The Less I Know the Better", "artist": "Tame Impala", "genre": "Alternative", "mood": "Energetic", "year": 2015},
    {"title": "Pumped Up Kicks", "artist": "Foster the People", "genre": "Alternative", "mood": "Happy", "year": 2010},
    {"title": "Feels Like We Only Go Backwards", "artist": "Tame Impala", "genre": "Alternative", "mood": "Chill", "year": 2012},
    {"title": "Fake Plastic Trees", "artist": "Radiohead", "genre": "Alternative", "mood": "Sad", "year": 1995},
]
while True:
    print("======================================")
    print("       ALBUM DISCOVERY GENERATOR")
    print("======================================")

    print()
    print("Discover albums based on your music preferences.")
    print()

    print("1. Find an album")
    print("2. Surprise me album")
    print("3. make my Ablum!! ")
    print("4. Exit")


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

        break


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
        break

    elif choice == "3":
        album_name = input("\nNAME UR ALBUM:")

        if album_name == "":
            album_name = "MY CUSTOM ABLUM"

        while True:
            album_size = input("HOW MUCH SONGS 1-"+ str(len(songs)) + "): ").strip()

            if album_size.isdigit() and 1 <= int(album_size) <= len(songs):
                album_songs = random.sample(songs, int(album_size))
                print("======================================")
                for song in album_songs:
                    print(song["title"], "-", song["artist"])

                break  # stop asking once we have a valid answer
            else:
                print("Invalid choice. Enter a number from 1 to", len(songs))

        links = []
        for song in album_songs:
            query = quote_plus(song["title"] + " " + song["artist"])
            links.append("https://www.youtube.com/results?search_query=" + query)

        filename = album_name.replace(" ", "_") + "_playlist.txt"
        with open(filename, "w") as f:
            f.write(album_name + "\n")
            for i in range(len(album_songs)):
                f.write(album_songs[i]["title"] + " - " + album_songs[i]["artist"] + "\n")
                f.write(links[i] + "\n")
        print("======================================")
        print("Saved to", filename)
        break


        
    elif choice == "4":
        print()
        print("Thanks for using Album Discovery Generator!")
        break

    else:
        print()
        print("Invalid choice.")