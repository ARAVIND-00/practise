def longest_unique_substring(s):
    print("start",len(s))
    start = 0
    seen = set()
    max_length = 0
    longest_start = 0  # To remember the starting index of the longest substring

    for end in range(len(s)):
        print("orginal",seen)
        # Shrink window from the left if current char is a duplicate
        while s[end] in seen:
            print("remove",s[start])
            seen.remove(s[start])
            start += 1

        seen.add(s[end])
        print("add",seen)

        current_window_length = end - start + 1
        print('this part')
        if current_window_length > max_length:
            max_length = current_window_length
            longest_start = start  # update starting index of max window

    longest_substring = s[longest_start:longest_start + max_length]
    return max_length, longest_substring

if __name__ == '__main__':
    s = "abcbcbb"
    longest_unique_substring(s)
