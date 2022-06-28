import clipboard
file = open("multiline_example.txt")
content = file.readlines()
result = ""
for line in content:
    result += line
print(result)
clipboard.copy(result[:-1])
