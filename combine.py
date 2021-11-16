filenames = ['a.txt', 'b.txt']

result = set()
for filename in filenames:
    with open(filename, encoding='utf-8') as file:
        add_set = set(file)
    result |= add_set

with open('combined.txt', 'w', encoding='utf-8') as file:
    file.writelines(result)