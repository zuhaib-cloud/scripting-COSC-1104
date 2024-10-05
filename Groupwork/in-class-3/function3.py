'''Course(1108-01): Scripting
Group: 01 , Date: 10/04/2024
Name: Mihir Mane(100947380), Zuhaib Khan(100935821)
'''

def gibi_to_giga(gib):
    return gib * 1_073_741_824 / 1_000_000_000

def giga_to_gibi(gb):
    return gb * 1_000_000_000 / 1_073_741_824

if __name__ == "__main__":
    # Test case for is_positive: 
    print(giga_to_gibi(10))
    print(gibi_to_giga(0))
    print(giga_to_gibi(22))
    print(gibi_to_giga(0.99))