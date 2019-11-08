from difflib import get_close_matches



# Driver program
if __name__ == "__main__":
    word = 'oh'
    patterns = ['oh', 'ohh', 'oho', 'puppy']
    print(get_close_matches(word, patterns))