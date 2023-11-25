import string
import re
from collections import Counter

def convert_to_regex(word_with_missing_letters):
    regex_pattern = ''.join(
        '[' + char.lower() + char.upper() + ']' if char.isalpha() else '[a-zA-Z]'
        for char in word_with_missing_letters
    )
    return regex_pattern

def guess(input_word):
  #Step 1
  default = []
  for n in range(len(input_word)-1, -1, -1):
      overlapping_slices = [input_word[i:i+n] for i in range(0, len(input_word)-n+1) if input_word[i:i+n].count('*') == 1]
      if overlapping_slices:
          default.extend(overlapping_slices)

  #Step 2
  alphabet_dict = {char: 0 for char in string.ascii_lowercase}

  #Step 3
  for word in default:
    user_index = word.index('*')
    prob_multiplier = len(word)/len(input_word)

    if(len(word) == 1):
      with open('/content/words_250000_train.txt', 'r') as file:
        words = file.read().lower().split()
      # Count the frequency of each letter
      counter = Counter(''.join(text))

      # Calculate the occurrence probability of each letter
      total_letters = sum(counter.values())
      occurrence_probability = {letter: count / total_letters for letter, count in counter.items()}

    else:
      pattern =  convert_to_regex(word)

      # Open the file and find all matching words
      with open('/content/words_250000_train.txt', 'r') as file:
        words = file.read().lower().split()
        matching_words = re.findall(pattern, ' '.join(words))

      # Extract letters at the user-provided index from matching_words
      letters_at_index = [word[user_index] for word in matching_words if len(word) > user_index]
      frequency_chart = Counter(letters_at_index)

      total_letters = len(letters_at_index)
      occurrence_probability = {letter: count / total_letters for letter, count in frequency_chart.items()}

    for key in occurrence_probability:
        occurrence_probability[key] *= prob_multiplier

    alphabet_dict = dict(Counter(alphabet_dict) + Counter(occurrence_probability))

  #Step 4
  return dict(sorted(alphabet_dict.items(), key=lambda item: item[1], reverse=True))

print(guess('o*a*ge'))
