line_of_words = input().split(" ")
lower_words = [w.lower() for w in line_of_words]
occurrences = {}
for word in lower_words:
    if word not in occurrences:
        occurrences[word] = 0
    occurrences[word] += 1
for word, occur in occurrences.items():
    if occur % 2 != 0:
        print(word, end=" ")
