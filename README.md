# Custom Word List Generator

This Python script generates a custom list of English words based on a set of user-defined criteria. It leverages the NLTK (Natural Language Toolkit) library's word corpus to filter and find words that match specific constraints regarding letter usage, letter priority, and word composition.

-----

## Features

  * **Letter Constraint**: Generate words using only a specific set of letters.
  * **Priority Letters**: Define a subset of "priority" letters.
  * **Unique Priority Count**: Set a minimum number of unique priority letters that must appear in each word.
  * **Priority Share**: Define a minimum percentage (share) of characters in each word that must be priority letters.
  * **Custom Output Size**: Specify the exact number of words you want in the final list.
  * **Randomization**: Optionally shuffle the resulting word list.

-----

## Requirements

  * Python 3
  * NLTK (`pip install nltk`)

-----

## How to Run

1.  **Install the NLTK library** if you haven't already:

    ```sh
    pip install nltk
    ```

2.  **Run the script** from your terminal:

    ```sh
    python word_generator.py
    ```

3.  **Download NLTK Data**: The first time you run the script, it will automatically download the required `words` corpus from NLTK.

4.  **Follow the Prompts**: The program will prompt you to enter your criteria in the terminal.

-----

## Usage Example

Here is an example of the program flow with user input and the resulting output.

### Input

```
Enter the letters you want to use: eniartos
Enter the priority letters: erta
Enter the minimum number of unique priority letters in each word: 3
Enter the minimum share of priority letters in each word (between 0 and 1): 0.5
Enter the number of words you want: 10
Do you want to shuffle the list? (y/n): y
```

### Output

```
Here are 10 words out of 579 meeting your criteria:
retirer otterer streeler tatter rester rainiest tetter iterate arsenite trierarch
```

In this example, the script found 579 words that could be formed from the letters `eniartos`. It then displayed 10 random words from that list where:

1.  At least 3 of the unique letters `e`, `r`, `t`, `a` were present.
2.  At least 50% of the characters in each word were from the set `e`, `r`, `t`, `a`.
