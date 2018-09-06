
each_word = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = each_word.get(word, 0)
    # Note: this is the "Look Before You Leap" (LBYL) pattern
    # we could use the "Easier to Ask Forgiveness" pattern using exceptions
    each_word[word] = frequency + 1

# Print the unique words and their frequencies,
# in alphabetical order
words = list(each_word.keys())
words.sort()
# use the max function to find the maximum of the values produced by the
# generator function (like a list comprehension) of lengths of words
max_length = max((len(word) for word in words))
for word in words:
print("{:{}} : {}".format(word, max_length, each_word[word]))