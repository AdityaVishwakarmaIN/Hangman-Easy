# Hangman-Easy

## Purpose

This code can play a game of hangman, given a word with blank positions and 6 guesses will return the best letter to guess.

## Methodology
* Identify all overlapping single wildcard slices in the input word. These provide clues for high probability letters.
* For each slice, calculate occurrence probability of each letter based on frequency in current dictionary (longer slices weighted higher).
* Aggregate occurrence probabilities across all slices into one alphabet dictionary.
* Sort the alphabet dictionary and return the highest probability letter.

## Example
* Game starts with an input_word = "o\*a\*ge"
* All overlapping single wildcard slices are identified. Each slice will have one vacant position only. ['a\*ge', 'o\*a', 'a\*g', '\*ge', 'o\*', '\*a', 'a\*', '\*g', '\*', '\*']
* For each slice, occurrence probability of each English alphabet is calculated, based on frequency in provided dataset (longer slices weighted higher).
* Every occurence probability is summed up into one alphabet dictionary. Initial value of alphabet dictionary was {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
* After sum, alphabet dictionary is sorted based on values and the highest probability letter is returned.

## Possible Improvements (Not Included)
* Exclude guess letters and letters already included in input_word before returning guess value.
* Create a filtered dictionary from provided dataset which only include words that match the length of len(input_word).
* Create an external memory for repeated variables.

## Test
The model is trained on a dictionary of 250,000 words and can win games of hangman at a 70% rate on this set. It also has a success rate of over 55% on completely new words (not included in training dataset).
