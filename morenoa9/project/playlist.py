from collections import deque


class Playlist:
    def __init__(self, name):
        self.name = name
        self.queue = deque()

    def add_song(self, song):
        self.queue.append(song)

    def remove_song(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def play(self):
        print("Playback Queue:")
        for song in self.queue:
            print(f"→ {song}")
