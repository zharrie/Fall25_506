import csv
from collections import defaultdict
from song import Song


class MusicLibrary:

    def __init__(self):
        self.songs_by_id = {}
        self.songs_by_artist = defaultdict(list)
        self.songs_by_genre = defaultdict(list)
        self.all_songs = []

    def load_from_file(self, filename):
        
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                song = Song(
                    int(row["id"]),
                    row["title"],
                    row["artist"],
                    row["genre"],
                    int(row["duration"]),
                    float(row["rating"]),
                    int(row["play_count"])
                )

                self.songs_by_id[song.id] = song
                self.songs_by_artist[song.artist].append(song)
                self.songs_by_genre[song.genre].append(song)
                self.all_songs.append(song)

    def display_library(self):
        for song in self.all_songs:
            print(song)

    def search_by_title(self, title):
       
        results = []
        for song in self.all_songs:
            if title.lower() in song.title.lower():
                results.append(song)
        return results

    def search_by_artist(self, artist):
       
        return self.songs_by_artist.get(artist, [])

    def search_by_genre(self, genre):
        
        return self.songs_by_genre.get(genre, [])
