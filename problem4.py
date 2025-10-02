"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""


def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""


    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    
    with open(filename) as f:
        text = f.read().split()

    return len(text)


def count_lines(filename):
    
    with open(filename) as f:
        lines = f.read().count(".")

    return lines


def count_characters(filename, include_spaces=True):
    with open(filename) as f:
        characters = f.read()
        
    if include_spaces:
        return len(characters)
        
    else:
        exclude_spaces = characters.replace(" ", "")

    return len(exclude_spaces)


def find_longest_word(filename):
    
    with open(filename) as f:
        longest_word = f.read()
        longest_word = longest_word.replace(","," ").replace("."," ").split()
        
    word = ""
    for i in longest_word:
        if len(i) > len(word):
             word = i
    return word


import string

frequency = {}

def word_frequency(filename):
    with open(filename) as f:
        text = f.read().lower()
        
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

    # TODO: Open file
    # TODO: Read all words
    # TODO: Convert to lowercase
    # TODO: Remove punctuation (use string.punctuation)
    # TODO: Count frequency of each word



def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()