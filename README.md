# Hangman Word Prediction Model

**Description:**

This Python code implements a **word prediction model** inspired by the classic game Hangman. Given a word with missing letters represented by asterisks ("*"), the model analyzes potential candidates and estimates the probability of each letter filling the missing slots.

**Key Features:**

- Leverages a pre-existing text file containing a large corpus of words (e.g., `/content/words_250000_train.txt`).
- Analyzes both single-letter and multi-letter candidates, aiming to prioritize single-letter candidates for their potential efficiency.
- Estimates letter probabilities based on the provided word's context and the frequency of letters in the corpus.

**Usage:**

1. **Ensure you have the required text file:** Replace `/content/words_250000_train.txt` with the actual path to your word list file.
2. **Import the code:** Include `import guess` in your Hangman game implementation.
3. **Call the `guess` function:** Pass the word with missing letters (e.g., `"o*a*ge"`) as an argument.
4. **Interpret the results:** The function returns a dictionary where the keys are letters and the values are their estimated probabilities of being the missing letter (e.g., `{'e': 0.875, 'a': 0.125}`). This information can be used to guide your next guess in the Hangman game.

**Potential Improvements (Not Included in This Code):**

- **Refine letter filtering:** Enhance the code to exclude guessed letters and letters already included in the input word before returning the final guess value.
- **Optimize word list:** Create a filtered dictionary from the provided dataset that only includes words matching the length of the input word, potentially reducing computational cost.
- **External memory:** Consider storing frequently used variables (e.g., loaded word list) in an external memory (e.g., a dictionary) to improve efficiency for multiple guess requests.

**Additional Notes:**

- While the model exhibits a 70% success rate on a 250,000-word training set and a 55% success rate on new words, its performance in real-world Hangman games may vary depending on word choice, game strategy, and implementation details.

**Example Usage:**

```python
import guess

word_with_blanks = "o*a*ge"
letter_probabilities = guess.guess(word_with_blanks)
print(letter_probabilities)  # Output: {'e': 0.875, 'a': 0.125}
```
