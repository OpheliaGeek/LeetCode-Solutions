"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 
Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


def wordPattern(pattern: str, s: str) -> bool:
    """
    Fanction, which takes pattern and s 
    and check if s follows the pattern
    """
    pattern = list(pattern)
    s = list(s.split(" "))
    if len(pattern) != len(s):
        return False
    else:
        word_dict = dict(zip(pattern, s))
        check_list = []
        for letter in pattern:
            check_list.append(word_dict[letter])
        if check_list != s or len(set(pattern)) != len(set(s)):
            return False
        return True


# Print results for some cases.
try:
    print(
        f"Case 1: pattern = 'abba', s = 'dog cat cat dog'. Output: {wordPattern('abba','dog cat cat dog')}")
    print(
        f"Case 2: pattern = 'abba', s = 'dog cat cat fish'. Output: {wordPattern('abba','dog cat cat fish')}")
    print(
        f"Case 3: pattern = 'aaaa', s = 'dog cat cat dog'. Output: {wordPattern('aaaa','dog cat cat dog')}")
    print(
        f"Case 4: pattern = 'abba', s = 'dog dog dog dog'. Output: {wordPattern('abba','dog dog dog dog')}")
except:
    print("ERROR")
