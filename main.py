def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
    return book

def count_words(book):
    return len(book.split())

def count_character_frequency(book):
    book = book.lower()
    frequency = {}
    for char in book:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == "__main__":
    book_content = main()
    word_count = count_words(book_content)
    print(f"Word count: {word_count}")
    
    character_frequency = count_character_frequency(book_content)
    print("--- Begin report of books/frankenstein.txt ---")
    for char, freq in character_frequency.items():
        print(f"The {char} was found {freq} times")
    print("--- End report ---")