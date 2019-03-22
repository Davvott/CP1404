continue_running = True
strings = []

while continue_running:
    user_input = input("Enter a string: ")
    if user_input == '':
        continue_running = False
    else:
        strings.append(user_input)

strings_repeated = []
for i in range(1, len(strings)):
    string = strings.pop()
    if string in strings:
        strings_repeated.append(string)

if strings_repeated:
    print("Strings repeated: ", end='')
    for word in set(strings_repeated):
        print('"' + str(word), end='" ')
else:
    print("No strings repeated")
