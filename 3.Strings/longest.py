def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return " "
    return max (words, key=len)
text = "Python programming is incredibly powerful"
longest = find_longest_word(text)
print(f"The longest word is:{longest}")