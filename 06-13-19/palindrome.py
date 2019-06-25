
def reverse (text):
    return text[::-1]

def checkPalindrome ():
    if reverse(new_phrase) == new_phrase:
        return True
    else:
        return False

print("\nThis program checks if a phrase you enter is a palindrome.")

while True:
    phrase = input("\nEnter 'E' to exit\nEnter a phrase to check if its a palindrome: ")
    new_phrase = phrase.replace(" ", "")
    if new_phrase.lower() == "e":
        break
    if checkPalindrome():
        print("\n'" + phrase + "' is a palindrome!")
    else:
        print("\n'" + phrase + "' is not a palindrome.")
