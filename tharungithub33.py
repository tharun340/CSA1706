def count_vowels(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
if __name__ == "__main__":
    test_strings = [
        "Hello World",
        "Prolog",
        "AEIOU",
        "Python Programming",
        ""
    ]

    for text in test_strings:
        print(f"Number of vowels in '{text}': {count_vowels(text)}")
