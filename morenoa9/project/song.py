class Song:
#Song class represents a single song. And each song object
#saves all the metadata for searching, sorting, etc

    def __init__(self, song_id, title, artist, genre, duration, rating, play_count):
        self.id = song_id #id's for songs

        self.title = title
        self.artist = artist #basic info from songs
        self.genre = genre


        #For duration I stored it in seconds so it can be easily 
        #sorted and compared
        self.duration = duration      # duration in seconds
        self.rating = rating          # float (0.0 - 5.0)
        #play_count tracks how often the song has been played
        self.play_count = play_count  # number of times played

    def __str__(self): #This method converts duration from seconds
        #into a mm:ss format
        minutes = self.duration // 60
        seconds = self.duration % 60
        return (
            f'"{self.title}" - {self.artist} '
            f'({self.genre}) - {self.rating}★ '
            f'[{minutes}:{seconds:02d}]'
        )
