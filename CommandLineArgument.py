# Read three strings as input
str1 = input().split("-")
str2 = input().split("-")
str3 = input().split("-")

happiness = 0

for num in str3:
    if num in str1:
        happiness += 1
    elif num in str2:
        happiness -= 1

print(happiness)