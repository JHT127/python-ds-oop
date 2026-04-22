from hash import HashTable

# Create a hash table
ht = HashTable(size=7, threshold=0.7)

# Insert some key-value pairs
print("Inserting items:")
items = [(50, 'Apple'), (700, 'Banana'), (76, 'Cherry'), (85, 'Date'), (92, 'Elderberry'), (99, 'Fig')]
for k, v in items:
    ht.insert(k, v)
    print(f"Inserted: {k} -> {v} (Load factor: {ht.load_factor():.2f})")

# Search for items
print("\nSearching:")
search_keys = [50, 92, 100]
for key in search_keys:
    result = ht.search(key)
    if result:
        print(f"Found: {key} -> {result.value}")
    else:
        print(f"Not found: {key}")

# Delete an item
print("\nDeleting 76:")
if ht.delete(76):
    print("Successfully deleted 76")
    print(f"Search for 76 now returns: {ht.search(76)}")
else:
    print("76 not found for deletion")

# Show current table state
print("\nCurrent table contents:")
for i, node in enumerate(ht.table):
    if node:
        print(f"Index {i}: {node.key} -> {node.value}")
    else:
        print(f"Index {i}: Empty")