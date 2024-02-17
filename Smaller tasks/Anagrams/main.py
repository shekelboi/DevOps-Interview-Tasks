def find_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Finds the anagrams of words and groups them together.
    :param strs: A list of words.
    :return: A list of lists of anagrams grouped together.
    """
    # Initializing a dictionary in which we will store the anagrams.
    anagram_dict = {}
    for word in strs:
        # The key in the dictionary will be the sorted value of the given word. E.g. 'cba' and 'bca' would become 'abc'.
        # This helps us group the anagrams together, since if we sort the anagrams of a word,
        # they all return the same word as a result.
        # The sorted characters are joined to form a string.
        key = "".join(sorted(word))
        # If they key is not in the dictionary, we are creating a new dictionary entry with that key and initialize
        # its value as a list only containing the current word.
        if key not in anagram_dict:
            anagram_dict[key] = [word]
        # If they key already exists in the dictionary, we append its value (a list of anagrams) by the current word.
        else:
            anagram_dict[key].append(word)
    # We return the list of values (a list of anagrams) in a list.
    return list(anagram_dict.values())


strs = ["eat", "tea", "ate", "tan", "nat", "bat", "batt"]
print(find_anagrams(strs))
