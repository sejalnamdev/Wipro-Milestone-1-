scores = list(map(int, input("Enter scores separated by spaces: ").split()))

unique_scores = list(set(scores))
unique_scores.sort()

print("Runner-up score:", unique_scores[-2])