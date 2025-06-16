
def clean_input(user_input):
    """
    Clean the input by removing spaces and converting to lowercase.
    """
    return ''.join(user_input.lower().split())

def reverse_with_slicing(text):
    """
    Reverse the string using slicing.
    """
    return text[::-1]

def reverse_with_loop(text):
    """
    Reverse the string using a for-loop.
    """
    reversed_text = ''
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def is_palindrome(original, reversed_str):
    """
    Check if the original string is equal to the reversed one.
    """
    return original == reversed_str

def main():
    user_input = input("Enter a string or number: ")

    cleaned_input = clean_input(user_input)

    reversed_slicing = reverse_with_slicing(cleaned_input)
    print("Reversed (slicing):", reversed_slicing)

    reversed_loop = reverse_with_loop(cleaned_input)
    print("Reversed (loop):   ", reversed_loop)

    if is_palindrome(cleaned_input, reversed_slicing):
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")

if __name__ == "__main__":
    main()
