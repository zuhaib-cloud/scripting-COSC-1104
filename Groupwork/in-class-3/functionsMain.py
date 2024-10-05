'''Course(1108-01): Scripting
Group: 01 , Date: 10/04/2024
Name: Mihir Mane(100947380), Zuhaib Khan(100935821)
'''
#incase the assignment required a seperate file to function

from function1 import is_positive
from function2 import is_palindrome
from function3 import gibi_to_giga,giga_to_gibi

if __name__ == "__main__":
    # Test case for is_positive:
    print(is_positive(10))      
    print(is_positive(-5.5))  
    print(is_palindrome("Hello"))                     
    print(is_palindrome("Madam"))  
    print(giga_to_gibi(10))
    print(gibi_to_giga(0.5))
