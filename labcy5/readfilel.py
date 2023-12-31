with open('mytxt.txt') as f:
    lines=[line for line in f]
print(lines)
#removing the new line characrers
with open('mytxt.txt') as f:
    lines=[line.rstrip() for line in f]
print(lines)
