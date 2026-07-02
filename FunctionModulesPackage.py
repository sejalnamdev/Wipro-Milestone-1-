def sort_colors(colors):
    color_list = colors.split("-")
    color_list.sort()
    return "-".join(color_list)

# Input
colors = input("Enter colors: ")

# Output
print(sort_colors(colors))