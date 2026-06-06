def count_vowels(s):
    vowel = 'aeiou'
    count = 0
    for v in s.lower():
        if v in vowel:
            count += 1
        
    return count

print(count_vowels('hello'))