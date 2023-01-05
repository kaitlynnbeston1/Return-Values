def album(name, artist):
    """Makes an album, neetly formatted."""
    newAlbum = {"name": name.title(), "artist": artist.title(),}
    return newAlbum


active = True
while active:
    albumName = input("What is the name of your album? ")
    albumArtist = input("Who is the artist? ")
    albOutput = album(albumName, albumArtist)
    print("Created the following album:")
    for key, value in albOutput.items():
        print(f"{key}: {value}")
    again = input("Would you like to create another album? Type y or n: ")
    if again == "y":
        continue
    elif again == "n":
        print("Goodbye!")
        break
    else:
        print("That is not a valid response. Please try again.")

