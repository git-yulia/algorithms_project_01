# Analysis of Algorithms, Fall 2018 
# Assignment 3: Shuffle-Checker 
# Team members: Yevhen Voitiuk, Julia Maliauka, Michael Petracca

# initially, check if the string contains invalid characters, or is not the right length to be a shuffle. 
# also ensure that the characters are from our desired alphabet 

# next, run the algorithm to verify the shuffle 

n = 'abcde'
m = 'fghi'

length_of_shuffle = len(n) + len(m)

valid_shuffle = 'abcdefghi'
invalid_shuffle = 'bcdghhi'

shuffle = invalid_shuffle

next_char_of_n = 0
next_char_of_m = 0

def check(next_char_of_n, next_char_of_m):
    if next_char_of_m + next_char_of_n == length_of_shuffle:
        return True 

    elif next_char_of_n < len(n) and n[next_char_of_n] == shuffle[next_char_of_n + next_char_of_m] and check(next_char_of_n + 1, next_char_of_m):
        return True
    
    elif next_char_of_m < len(m) and m[next_char_of_m] == shuffle[next_char_of_n + next_char_of_m] and check(next_char_of_n, next_char_of_m + 1):
        return True

    return False 
    
print(check(next_char_of_n, next_char_of_m))