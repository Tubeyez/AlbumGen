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