# to check whether strings are anagrams or not.
def are_anagrams(str1 , str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return sorted(str1) == sorted(str2)
word1 = input("Enter the first string:")
word2 = input("Enter the second string:")

if are_anagrams(word1 , word2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")

