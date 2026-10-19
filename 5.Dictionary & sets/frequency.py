def count_word_frequency(sentence):
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "Hello word hello"
print(count_word_frequency(text))