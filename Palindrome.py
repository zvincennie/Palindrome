from stack import Stack

def isPalindrome(sentence):
    """Returns True if sentence is a palindrome or False otherwise."""
    stk = Stack()  # Creates a stack called stk.

    # Remove spaces and punctuation and convert to lowercase
    sentence = ''.join(e for e in sentence if e.isalnum()).lower()

    # Push each character onto the stack
    for char in sentence:
        stk.push(char)

    reversed_sentence = ""
    
    # Pop characters from the stack in reverse order
    while not stk.isEmpty():
        reversed_sentence += stk.pop()

    # Check if the original and reversed sentences are the same
    return sentence == reversed_sentence

# Do not modify main()
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")

main()
