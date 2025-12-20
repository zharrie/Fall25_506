from collections import defaultdict, deque


class RecommendationGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def build_graph(self, songs):
        for song in songs:
            for other in songs:
                if song != other and song.genre == other.genre:
                    self.graph[song.id].append(other)

    def recommend(self, song_id, limit=5):
        visited = set()
        queue = deque([song_id])
        recommendations = []

        while queue and len(recommendations) < limit:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor.id not in visited:
                    visited.add(neighbor.id)
                    recommendations.append(neighbor)
                    queue.append(neighbor.id)

        return recommendations
