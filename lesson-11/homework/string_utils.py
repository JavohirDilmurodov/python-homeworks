#2. Create string_utils.py module. Define `reverse_string` and `count_vowels` functions in it. 
#(All functions accept one argument in this task)

def reverse_string(txt : str):
    rev_txt = txt[::-1]
    return rev_txt

def count_vowels(txt1 : str):
    vowels = "aeiouAEIOU"  
    return sum(1 for char in txt1 if char in vowels)


