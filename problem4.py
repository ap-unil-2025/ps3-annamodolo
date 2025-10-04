"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""
import string
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

    with open(filename, 'w' , encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """
    Count total words in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    words = text.split()
    return len(words)


def count_lines(filename):
    """
    Count total lines in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return len(lines)

def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.
    If include_spaces is False, don't count spaces.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    if not include_spaces:
        text = text.replace(" ", "")
    return len(text)

def find_longest_word(filename):
    """
    Find and return the longest word in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().split()
    longest = max(words, key=len)
    return longest



def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    # Remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


def analyze_file(filename):
    """
    Perform complete analysis of the file.
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        print("\nTop 5 most common words:")
        freq = word_frequency(filename)
        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except ImportError as e:
        print(f"Error: {e}")


def main():
    """Main function to create and analyze text files."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "-" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()
