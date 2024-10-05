'''Course(1108-01): Scripting
Group: 01 , Date: 10/04/2024
Name: Mihir Mane(100947380), Zuhaib Khan(100935821)
'''

def is_positive(num):
    while isinstance(num, (int, float)): 
        # if the number is positive
        if num > 0:
            return True
            
        # if the number is negative or zero
        elif num <= 0:
            return False

if __name__ == "__main__":
    # Test case for is_positive:
    print(is_positive(10))      
    print(is_positive(-5.5)) 
    print(is_positive(0))      
    print(is_positive(-50000)) 
    print(is_positive(1.9999))      
    print(is_positive("test"))   