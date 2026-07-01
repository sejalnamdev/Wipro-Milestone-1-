# Dictionary containing student names and their marks
students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

# Get the student's name
name = input("Enter a name: ")

# Calculate and display the average marks
marks = students[name]
average = sum(marks) / len(marks)

# Print average
print("Average percentage mark:", int(average))

#OUTPUT:
Enter a name: Malika
Average percentage mark: 56