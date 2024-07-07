def ten_cap(word):
    """
    Write a function that takes a string as an argument 
    and returns an all-caps version of the string when 
    the string is longer than 10 characters. Otherwise, 
    it should return the original string. 
    """
    if len(word) > 10:
        return word.upper()
    else:
        return word

word = input("Enter a word: ")
print(ten_cap(word))