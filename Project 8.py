def ispalindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in name:
        if ch in vowels:
            count += 1
    print("No of vowels:", count)


def frequency_of_letters(name):
    freq = {}
    for ch in name:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1

    print("Frequency of letters:", end=" ")
    first = True
    for key, value in freq.items():
        if not first:
            print(", ", end="")
        print(f"{key}-{value}", end="")
        first = False
    print()

#MAIN.PY
import mymodule

name = input("Enter a name: ")

mymodule.ispalindrome(name)
mymodule.count_the_vowels(name)
mymodule.frequency_of_letters(name)