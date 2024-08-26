def find_repeated_substrings(s: str) -> list:
    substring_count = {}
    n = len(s)
    
    # Generate all possible substrings of length 2 or more
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = s[i:j]
            if substring in substring_count:
                substring_count[substring] += 1
            else:
                substring_count[substring] = 1
    
    # Collect substrings that appear more than once
    repeated_substrings = [substring for substring, count in substring_count.items() if count > 1]
    
    return repeated_substrings


print(find_repeated_substrings("banana"))# Output: ['an', 'ana', 'na']

print(find_repeated_substrings("abcdefg"))# Output: []

print(find_repeated_substrings("abcabcabc"))# Output: ['ab', 'abc', 'abca', 'abcab', 'abcabc', 'bc', 'bca', 'bcab','bcabc', 'ca', 'cab', 'cabc ']

print(find_repeated_substrings("aaaa"))# Output: ['aa', 'aaa ']