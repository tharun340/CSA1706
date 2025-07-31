def sort_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    return ' '.join(words)

def main():
    sentence = input("Enter a sentence: ")
    sorted_sentence = sort_sentence(sentence)
    print("Sorted sentence:")
    print(sorted_sentence)

if __name__ == "__main__":
    main()
