with open("6.Read files/sample.txt" , "r") as file:
    text = file.read()
words = text.split()
print("Total number of words:" , len(words))