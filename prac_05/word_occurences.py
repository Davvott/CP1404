from string import punctuation
# Prompt user for string
text_string = input("Enter a sentence or paragraph: ")
# text_string = "this is a collection of words of nice words this is a fun thing it is"

for char in punctuation:
    text_string.replace(char, '')

word_list = text_string.split()

# Create dictionary of {word: count}
word_count ={}
for word in word_list:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1
# Sort list of keys
sort_list = sorted(word_count)

# Print sorted counts of each word
for key in sort_list:
    print("{} : {}".format(key, word_count[key]))

# Pretty printing
max_length_key = max([len(key) for key in word_count])

print("Text: a fun collection")
for key in sort_list:
    print("{:{}} : {}".format(key, max_length_key, word_count[key]))

# Super pretty printing
print("Text: a fun collection")
for key in sort_list:
    print("{:>{}} : {}".format(key, max_length_key, word_count[key]))
