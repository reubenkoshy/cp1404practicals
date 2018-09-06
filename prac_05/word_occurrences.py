
each_word = {}
text = input("Text: ")
words = text.split()
for word in words:
    occurrences = each_word.get(word, 0)

    each_word[word] = occurrences + 1

words = list(each_word.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, each_word[word]))

