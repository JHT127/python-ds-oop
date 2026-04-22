
""" City Map Class"""

from graph import Graph

class CityMap:
    def __init__(self):
        self.graph = Graph()

    def add_location(self, label):
        """Add a new location to the city map"""
        self.graph.add_vertex(label)

    def remove_location(self, label):
        """Remove a location from the city map"""
        self.graph.remove_vertex(label)

    def add_road(self, src, dest, time):
        """Add a one-way road between locations with travel time"""
        self.graph.add_edge(src, dest, time)

    def remove_road(self, src, dest):
        """Remove a one-way road between locations"""
        self.graph.remove_edge(src, dest)

    def shortest_path(self, start_label, end_label):
        """
        Find the shortest path between two locations using Dijkstra's algorithm
        Returns the path and total travel time
        """
        start = self.graph.find_vertex(start_label)
        end = self.graph.find_vertex(end_label)

        if not start or not end:
            return None, float('inf')

        # Step 1: Initialize distances
        distances = {v.label: float('inf') for v in self.graph.vertices}
        distances[start_label] = 0
        previous = {v.label: None for v in self.graph.vertices}
        unvisited = {v.label for v in self.graph.vertices}

        while unvisited:
            # Step 2/6: Select unvisited vertex with smallest distance
            current_label = min(unvisited, key=lambda x: distances[x])
            # key=lambda x: distances[x] is equivalent to:
            # lambda x: = "for each element x"
            # distances[x] = "look up x's distance"
            # key= = "use this value for comparisons"
            # So it means: "When finding the minimum, compare the distance values rather than the elements themselves.
            current = self.graph.find_vertex(current_label)
            unvisited.remove(current_label)

            # Early exit if we've reached the destination
            if current_label == end_label:
                break

            # Step 3: Consider all unvisited neighbors
            for edge in current.edges:
                neighbor = edge.target
                if neighbor.label not in unvisited:
                    continue

                # Step 4: Calculate tentative distance
                alt_distance = distances[current_label] + edge.weight

                # Update if better path found
                if alt_distance < distances[neighbor.label]:
                    distances[neighbor.label] = alt_distance
                    previous[neighbor.label] = current_label

        # Reconstruct path
        path = []
        current_label = end_label
        while previous[current_label] is not None:
            path.insert(0, current_label)
            current_label = previous[current_label]

        if path or start_label == end_label:
            path.insert(0, start_label)
            # The 0 means:
            # Insert at position 0 (the very start of the list)
            # This builds the path in reverse order (from destination back to start)
            # Without it, the path would be backwards
            return path, distances[end_label]
        else:
            return None, float('inf')

    def reachable_locations(self, start_label):
        """List all reachable locations from a starting point using BFS"""
        self.graph.bfs(start_label)

    def __str__(self):
        return str(self.graph)
