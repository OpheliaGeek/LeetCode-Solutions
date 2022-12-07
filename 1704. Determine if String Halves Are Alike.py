"""
You are given a string s of even length. 
Split this string into two halves of equal lengths, 
and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels 
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""


def split_string_into_two(s: str) -> str:
    """
    Split given string into two halves of equal lengths
    """
    first_half = s[0:(int(len(s)/2))]
    second_half = s[(int(len(s)/2)):len(s)]
    return first_half, second_half


def number_of_vowels(any_str: str) -> int:
    """
    Count number of vowels in given word
    """
    count = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in any_str:
        if letter in vowels_list:
            count += 1
    return count


def enter_str() -> str:
    """
    Take a string from user and check it lenght
    """
    while True:
        s = input("Please enter a string with even lenght = ")
        if len(s) % 2 == 0:
            break
        else:
            print("Error. Lenght is not even")
    return s


def is_it_alike(a: str, b: str) -> bool:
    """
    Check Two strings, they are alike if they have the same number of vowels
    """
    return number_of_vowels(a) == number_of_vowels(b)


s = enter_str()
a, b = split_string_into_two(s)
result = is_it_alike(a, b)
print(result)
