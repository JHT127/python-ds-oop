
""" Main - Graph Implementation for Palestinian Cities """

from city_map import CityMap

def main():
    # ==============================================
    # TASK 1: Class-based graph implementation
    # (Demonstrated by using CityMap class)
    # ==============================================
    city_map = CityMap()

    # ==============================================
    # TASK 2: Populate with 6+ locations and 10+ roads
    # ==============================================
    # Add 7 locations
    locations = [
        "Al-Quds",
        "Ramallah",
        "Nablus",
        "Hebron",
        "Gaza",
        "Bethlehem",
        "Jenin"
    ]

    for location in locations:
        city_map.add_location(location)

    # Add 10 roads
    roads = [
        ("Al-Quds", "Ramallah", 15),
        ("Ramallah", "Nablus", 45),
        ("Nablus", "Jenin", 30),
        ("Al-Quds", "Bethlehem", 10),
        ("Bethlehem", "Hebron", 20),
        ("Hebron", "Gaza", 90),
        ("Gaza", "Al-Quds", 75),
        ("Ramallah", "Bethlehem", 25),
        ("Nablus", "Hebron", 60),
        ("Jenin", "Nablus", 30)
    ]

    for src, dest, time in roads:
        city_map.add_road(src, dest, time)

    print("=== Current City Map ===")
    print(city_map)

    # ==============================================
    # TASK 3A: Add/remove locations and roads
    # ==============================================
    print("\n=== Testing Location/Road Modifications ===")

    # Add new location
    print("\nAdding new location: Jericho")
    city_map.add_location("Jericho")

    # Add new road
    print("Adding new road: Jericho to Ramallah (35 mins)")
    city_map.add_road("Jericho", "Ramallah", 35)

    # Remove road
    print("\nRemoving road: Nablus to Hebron")
    city_map.remove_road("Nablus", "Hebron")

    # Remove location (will automatically remove connected roads)
    print("Removing location: Jenin")
    city_map.remove_location("Jenin")

    print("\n=== Updated City Map ===")
    print(city_map)

    # ==============================================
    # TASK 3B: Shortest path (Dijkstra's algorithm)
    # ==============================================
    print("\n=== Testing Shortest Paths ===")

    # Simple path
    path, time = city_map.shortest_path("Al-Quds", "Bethlehem")
    print(f"\nAl-Quds -> Bethlehem: {path}, {time} mins")

    # Multi-hop path
    path, time = city_map.shortest_path("Ramallah", "Gaza")
    print(f"Ramallah -> Gaza: {path}, {time} mins")

    # No path exists
    path, time = city_map.shortest_path("Gaza", "Jericho")
    print(f"Gaza -> Jericho (no path): {path}, {time} mins")

    # ==============================================
    # TASK 3C: Reachable locations (BFS)
    # ==============================================
    print("\n=== Testing Reachable Locations ===")

    print("\nFrom Al-Quds:")
    city_map.reachable_locations("Al-Quds")

    print("\nFrom Gaza:")
    city_map.reachable_locations("Gaza")

    print("\nFrom Jericho (newly added):")
    city_map.reachable_locations("Jericho")


if __name__ == "__main__":
    main()