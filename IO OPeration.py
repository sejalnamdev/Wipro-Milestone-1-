from collections import Counter
import re

# Open the file
with open("sample.txt", "r") as file:
    lines = file.readlines()

# Meeting time
n = len(lines)

if n <= 12:
    time = f"{n} AM"
else:
    time = f"{n - 12} PM"

# Count word frequency
text = " ".join(lines)
words = re.findall(r"[A-Za-z]+", text)

freq = Counter(word.lower() for word in words)

# Most frequent word
place = max(freq, key=freq.get).capitalize()

print("Meeting time:", time)
print("Meeting place:", place + " Street")