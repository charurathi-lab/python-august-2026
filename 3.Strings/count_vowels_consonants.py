str = "Python Programming"
text = str.lower()
vowels_count = sum(1 for char in text if char in "aeiou")
consonants_count = sum( 1 for char in text if char.isalpha() and char not in "aeiou")
print (f" Vowels = {vowels_count}")
print(f" Consonats = {consonants_count}")