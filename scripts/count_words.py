import sys
import os
import re

def count_stats(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Fallback for other encodings if utf-8 fails
        with open(file_path, 'r', encoding='cp949') as f:
            content = f.read()

    # Character count (including spaces)
    char_count_with_spaces = len(content)
    
    # Character count (excluding spaces/newlines)
    char_count_no_spaces = len(content.replace(" ", "").replace("\n", "").replace("\r", ""))
    
    # Word count (splitting by whitespace)
    words = content.split()
    word_count = len(words)
    
    print(f"File: {os.path.basename(file_path)}")
    print("-" * 30)
    print(f"Characters (including spaces): {char_count_with_spaces:,}")
    print(f"Characters (excluding spaces): {char_count_no_spaces:,}")
    print(f"Word count: {word_count:,}")
    print("-" * 30)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/count_words.py <filename>")
    else:
        count_stats(sys.argv[1])
