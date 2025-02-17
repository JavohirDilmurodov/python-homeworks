def count_vowels(txt1 : str):
    vowels = "aeiouAEIOU"  
    return sum(1 for char in txt1 if char in vowels)


text = "Hello, World!"
print(count_vowels(text)) 