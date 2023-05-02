''' palindrome, by definition, is a word that is same as its reverse word'''

w = str(input("Type the word: "))
if w[::-1] == w:
    print('It is a palindrome')
else:
    print('It is not a palindrome')
