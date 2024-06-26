"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

def minion_game(string):
    # your code goes here
    word_vowel_list = []
    word_consonant_list = []
    player_1 = "Stuart"
    player_2 = "Kevin"
    vowel_list=["a","e","i","o","u"]

    # Kevin turn
    for i in range(len(string)):
        if(string[i] in vowel_list):
            word_vowel_list.append(string[i])
        else:
            word_consonant_list.append(string[i])



s = input()
minion_game(s)