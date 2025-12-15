# ======================
# Core domain classes
# ======================

from verbose import verbose_log


class Song:
    """
    Represents a single song in the music library.

    Attributes:
        song_id: string identifier (for example: "1", "2", "A15")
        title: song title (string)
        artist: artist name (string)
        genre: genre name (string)
        duration_in_seconds: integer duration in seconds
        rating: float rating (for example: 4.5)
        play_count: integer, how many times the song has been played
    """

    def __init__(self, song_id, title, artist, genre, duration_in_seconds, rating, play_count):
        self.song_id = song_id  # store the id exactly as given so other modules can reference it
        self.title = title  # store the title for display, sorting, and searching
        self.artist = artist  # store the artist name for display and searching
        self.genre = genre  # store the genre name for display and searching
        self.duration_in_seconds = duration_in_seconds  # store duration as seconds because it's to compute
        self.rating = rating  # store rating as a float, so we can show decimals like 4.5
        self.play_count = play_count  # store play count, so the project can track popularity
        self.norm_genre = genre.lower()  # store a normalized genre to make case-insensitive comparisons
        self.norm_artist = artist.lower()  # store a normalized artist to make case-insensitive comparisons

    def __str__(self):
        """
        Return a human-readable description of the song.
        """
        description = "\"" + self.title + "\" | " + self.artist
        description += " (" + self.genre + ") | "
        description += f"{self.rating:.1f}★ | "
        description += "[" +  format_duration(self.duration_in_seconds) + "]"
        return description


def format_duration(seconds):
    """
    Convert an integer number of seconds to "M:SS" string.

    seconds: integer
    returns: string
    """
    minutes = seconds // 60  # get whole minutes using floor division
    remaining_seconds = seconds % 60  # get leftover seconds with modulus
    return f"{minutes}:{remaining_seconds:02d}"  # return time in MM:SS format


# ======================
# Playlist
# ======================

class Playlist:
    """
    Represents a playlist of songs.

    Attributes:
        name: playlist name (string)
        song_list: list of Song objects
    """

    def __init__(self, name):
        self.name = name  # store the playlist name so menus and output can identify it
        self.song_list = []  # start with an empty list because the playlist begins with no songs
        verbose_log("Created new playlist with name '" + self.name + "'.")

    ## implement partial string match here

    def add_song(self, song):
        """
        Add a song to the playlist.

        song: Song
        """
        self.song_list.append(song)  # append keeps insertion order, expected behavior in a playlist
        verbose_log(
            "Added song '"
            + song.title
            + "' to playlist '"
            + self.name
            + "'. Playlist now has "
            + str(len(self.song_list))
            + " song(s)."
        )

    def remove_song_by_title(self, title):
        """
        Remove the first song whose title matches the given string.

        title: string
        returns: True if a song was removed, False otherwise
        """
        title_lower = title.lower()  # normalize the input title, so matching is case-insensitive
        index = 0  # set initial index to zero so we start scanning from the beginning
        while index < len(self.song_list):  # loop through the list one position at a time until we hit the end
            song = self.song_list[index]  # get the current song at this index so we can check its title
            if song.title.lower() == title_lower:  # compare normalized titles so "Halo" and "halo" match
                verbose_log(
                    "Removing song '"
                    + song.title
                    + "' from playlist '"
                    + self.name
                    + "'."
                )
                del self.song_list[index]  # delete the matching song (this shifts later items left, which is fine)
                return True  # return True immediately because we only remove the first match
            index += 1  # move to the next index if we did not find a match at the current position

        verbose_log(
            "Requested removal of song titled '"
            + title
            + "' from playlist '"
            + self.name
            + "', but it was not found."
        )
        return False  # return False to indicate no song was removed

    def total_duration(self):
        """
        returns: total duration (in seconds) of all songs in this playlist
        """
        total = 0  # start at zero because we are going to add each song's duration into this accumulator
        for song in self.song_list:  # loop through each song because a playlist total depends on all entries
            total = total + song.duration_in_seconds  # add this song's seconds to the running total
        return total  # return the final computed duration in seconds

    def __str__(self):
        """
        Return a human-readable description of the playlist.
        """
        if not self.song_list:
            return 'Playlist "' + self.name + '" is empty.'
        output_lines = [
            'Playlist "'
            + self.name
            + '" ('
            + str(len(self.song_list))
            + " songs, "
            + format_duration(self.total_duration())
            + " total):"
        ]

        for song in self.song_list:  # loop through songs in order so the printed playlist matches the stored order
            output_lines.append("  " + str(song))  # indent each song line to visually show it belongs to the playlist

        return "\n".join(output_lines)  # join all lines with newlines to make a multi-line printable string