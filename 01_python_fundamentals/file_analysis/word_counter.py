
import os

file = input("Please enter file name:  ")

if not os.path.exists(file):
    print("Error: File not found.")
    exit()

with open (file, mode="r") as f:
    lines = f.readlines()
    f.close()

words = []
for line in lines:
    words.extend(line.split())

print (f"The number of words in the file is {len(words)}.")

word_counts = {}
frequent_word_count = 0
most_frequent_word = None

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

    if word_counts[word] > frequent_word_count:
        most_frequent_word = word
        frequent_word_count = word_counts[word]

print(f"The most frequent word is '{most_frequent_word}' and it appears {frequent_word_count} times.")

with open ("output_word_counter.txt", "w") as o:
    o.write(f"The number of words in the file is {len(words)}.\n")
    o.write(f"The most frequent word is '{most_frequent_word}' and it appears {frequent_word_count} times.")
    f.close()
    print("\nCheck the output_word_counter.txt file!")


