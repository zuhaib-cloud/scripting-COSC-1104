'''Course(1108-01): Scripting
Group: 01 , Date: 10/04/2024
Name: Mihir Mane(100947380), Zuhaib Khan(100935821)
'''

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    # Test case for is_positive: 
    print(is_palindrome("Hello"))                     
    print(is_palindrome("Madam"))  
    print(is_palindrome("Ronaldo"))                     
    print(is_palindrome("Messi")) 
    print(is_palindrome("ikikiki"))                     
