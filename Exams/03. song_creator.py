def add_songs(*songs):
    songs_dict = {}
    result = ""
    for song in songs:
        title, lyrics = song
        if title in songs_dict:
            songs_dict[title] += lyrics
        else:
            songs_dict[title] = lyrics
    for title, lyrics in songs_dict.items():
        result += "- {}\n".format(title)
        if lyrics:
            for line in lyrics:
                result += "{}\n".format(line)
    return result



print(add_songs(

    ("Beat It", []),

    ("Beat It",

     ["Just beat it (beat it), beat it (beat it)",

      "No one wants to be defeated"]),

    ("Beat It", []),

    ("Beat It",

     ["Showin' how funky and strong is your fight",

      "It doesn't matter who's wrong or right"]),

))