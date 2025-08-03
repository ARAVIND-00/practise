def length_of_longest_substring(s):
    char_set = set()
    max_len = 0
    start = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_len = max(max_len, end - start + 1)
    print(max_len)
    return max_len



length_of_longest_substring("abcbfg")
