# Explanation:
- Mapping Dictionary: english_to_arabic contains the mappings from English keys to Arabic letters based on their positions on the keyboard.
- Decode Function: The decode_word(encoded_word) function takes an encoded word (string) and iterates through each character. If the character exists in the english_to_arabic dictionary, it replaces it with the corresponding Arabic letter. If the character doesn't exist in the dictionary (like spaces or punctuation), it leaves it unchanged.
- User Input and Output: The program prompts the user to input an encoded word, decodes it, and then prints the decoded Arabic text.

# Example
- Input : "hgsbl ugd;l"
- Output : "السلام عليكم"

# Goal:
- The goal of the program is when we write in Arabic while forgetting to change the keyboard language from English to Arabic
