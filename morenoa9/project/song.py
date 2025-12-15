class Song:

    def __init__(self, song_id, title, artist, genre, duration, rating, play_count):
        self.id = song_id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration      # duration in seconds
        self.rating = rating          # float (0.0 - 5.0)
        self.play_count = play_count  # number of times played

    def __str__(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return (
            f'"{self.title}" - {self.artist} '
            f'({self.genre}) - {self.rating}★ '
            f'[{minutes}:{seconds:02d}]'
        )
