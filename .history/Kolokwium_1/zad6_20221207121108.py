# define a list of Polish vowels
polish_vowels = ['a', 'e', 'i', 'o', 'u', 'ą', 'ę', 'ó']

# get the text to count the vowels in
text = input('Enter the text to count the vowels in: ')
text.lower()
# split the text into a list of words
words = text.split()

# initialize a dictionary to store the number of vowels in each word
vowel_counts = {}

# loop through each word in the list
for word in words:
    # initialize a counter for the number of vowels in the current word
    vowel_count = 0

    # loop through each character in the word
    for char in word:
        # check if the character is a Polish vowel
        if char in polish_vowels:
            # if it is, increment the vowel counter
            vowel_count += 1

    # add the number of vowels in the current word to the dictionary
    vowel_counts[word] = vowel_count

# print the number of vowels in each word
for word, count in vowel_counts.items():
    print(f'The number of Polish vowels in "{word}" is: {count}')

# initialize a counter for the total number of vowels
total_vowel_count = 0

# loop through each word in the dictionary and add the number of vowels in each word to the total
for word, count in vowel_counts.items():
    total_vowel_count += count

# print the total number of vowels in the text
print('The total number of Polish vowels in the given text is:', total_vowel_count)
