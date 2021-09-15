wrd=input("Please enter a word: ")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a Palindrome")
else:
    print("This word is not a palindrome")