def makeAlbum(name, artist, songs = None):
    """Makes an album."""
    newAlbum = {"name": name.title(), "artist": artist.title(),}
    if songs:
        newAlbum["songs"] = songs
    return newAlbum


pop = makeAlbum("midnights", "taylor swift")
metal = makeAlbum("final days", "orden ogan", 12)
random = makeAlbum("system failure", "kaitlynn beston", 13)


for key, value in pop.items():
    print(f"{key}: \t {value}")
print("\n \n \n")
for key, value in metal.items():
    print(f"{key}: \t {value}")
print("\n \n \n")
for key, value in random.items():
    print(f"{key}: \t {value}")