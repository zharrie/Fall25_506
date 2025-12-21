# ======================
# Graph for similarity + BFS recommendations
# ======================

from collections import defaultdict, deque  # supports queue behavior for BFS
from verbose import verbose_log  # verbose logging utility used throughout the project
#from models import Song  # imported for type context (Song objects are used in build_from_songs)


class SongGraph:
    """
    Simple undirected similarity graph.

    Vertices: song_id strings
    Edges: songs that share the same artist or the same genre

    Attributes:
        adjacency_list: dictionary mapping song_id to list of neighbor song_ids
    """

    def __init__(self):
        self.adjacency_list = defaultdict(list)  # use lists for neighbors to match adjacency-list representation
        verbose_log("Initialized empty SongGraph.")

    def add_edge(self, song_id_a, song_id_b):
        """
        Add an undirected edge between two songs.

        song_id_a: string
        song_id_b: string
        """
        if song_id_b not in self.adjacency_list[song_id_a]:  # avoid duplicate neighbor entries so the adjacency list stays clean
            self.adjacency_list[song_id_a].append(song_id_b)  # add B to A's neighbor list (one direction of undirected edge)
        if song_id_a not in self.adjacency_list[song_id_b]:  # avoid duplicate neighbor entries in the reverse direction
            self.adjacency_list[song_id_b].append(song_id_a)  # add A to B's neighbor list (other direction of undirected edge)

    def build_from_songs(self, song_list):
        """
        Build similarity edges based on:
        - Same artist
        - Same genre

        song_list: list of Song
        """
        verbose_log("Building song similarity graph based on artist and genre.")

        songs_grouped_by_artist = defaultdict(list)  # group songs by artist to connect artists's songs together
        songs_grouped_by_genre = defaultdict(list)  # group songs by genre to connect songs by genre

        for song in song_list:  # go through every Song so we can place it into the correct group
            songs_grouped_by_artist[song.artist].append(song.song_id)  # this will set it up so the key is the artist and all songs by that artist are under that key
            songs_grouped_by_genre[song.genre].append(song.song_id)  # this sets it up so the key is the genre and all songs under that genre are the values
        
        # now connect songs with the same artist
        for songs_by_same_artist in songs_grouped_by_artist.values():  # each value is a list of the song ids that share one artist
            for i in range(len(songs_by_same_artist)):  # pick the first song as a vertex to connect
                for j in range(i + 1, len(songs_by_same_artist)):  # pick the second song, index_a+1 to avoid repeats
                    self.add_edge(songs_by_same_artist[i], songs_by_same_artist[j])  # this adds an undirected edge between the pair

        # and connect songs with the same genre
        for songs_with_same_genre in songs_grouped_by_genre.values():  # each value is a list of the songs ids that have the same genre
            for i in range(len(songs_with_same_genre)):  # pick the first song as a vertex to connect
                for j in range(i + 1, len(songs_with_same_genre)):  # choose the second song after index_a
                    self.add_edge(songs_with_same_genre[i], songs_with_same_genre[j])  # add the undirected edge

        verbose_log(
            "SongGraph built with "  
            + str(len(self.adjacency_list)) 
            + " nodes connected by similarity edges."  
        )

    def recommend_using_breadth_first_search(self, start_song_id, maximum_depth=2, maximum_results=5): 
        # for recs, we only want to visit up to a certain # of "visitors" instead of every visitor so we only make the more relevant recommendations
        """
        Perform BFS from start_song_id to find recommended songs.

        start_song_id: string (a song)
        maximum_depth: integer (maximum BFS depth)
        maximum_results: integer (maximum number of recommendations)
        returns: list of song_id strings
        """
        if start_song_id not in self.adjacency_list:  # if the start node is not in the graph, BFS can't begin
            verbose_log(
                "Starting song id "
                + start_song_id 
                + " not present in SongGraph; no recommendations will be generated."
            )
            return []  # no start node means no recommendations :(

        visited_song_ids = set([start_song_id])  # discovered set starts with the start node
        frontier_queue = deque([(start_song_id, 0)])  # this is the frontier queue, deque is part of the collections import and allows a double sided queue which is good for removing and adding to the queue as is needed for BFS
        recommended_song_ids = []  # list to save recommendations in the order we discover them

        verbose_log(
            "Starting BFS recommendations from song id "  
            + start_song_id 
            + " (maximum_depth="  
            + str(maximum_depth)  
            + ")." 
        )

        while frontier_queue and len(recommended_song_ids) < maximum_results:  # BFS will loop while frontier is not empty and we still need results
            current_song_id, current_depth = frontier_queue.popleft()  # dequeue the next vertex to visit

            if current_depth >= maximum_depth:  # if we've reached the max depth, don't keep going
                pass  # don't go because BFS would go deeper than allowed

            for neighbor_song_id in self.adjacency_list[current_song_id]:  # iterate through adjacency list neighbors
                if neighbor_song_id not in visited_song_ids:  # only process undiscovered nodes so we don't loop forever
                    visited_song_ids.add(neighbor_song_id)  # vertex becomes part of discovered
                    frontier_queue.append((neighbor_song_id, current_depth + 1))  # enqueue next vertex with depth+1 to explore next layer
                    recommended_song_ids.append(neighbor_song_id)  # append the recommendation to our list from earlier
                    verbose_log(
                        "BFS discovered neighbor "
                        + neighbor_song_id  
                        + " at depth "  
                        + str(current_depth + 1)  
                        + "." 
                    )
                    if len(recommended_song_ids) >= maximum_results:  # if we reached the requested number of recommendations stop 
                        break 
                    
        verbose_log(
            "BFS recommendation traversal produced "  
            + str(len(recommended_song_ids))  
            + " candidate songs."  
        )
        return recommended_song_ids  # return the list recommended song ids
