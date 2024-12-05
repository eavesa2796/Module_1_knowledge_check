####################
# Check if number is even or odd
def even_or_odd(number):
    #check if the number divided by 2 has a remainder of 0
    if number % 2 == 0:
        return "Even"
    #if the check for remainder of 0 is false then it is odd
    else:
        return "Odd"
        
even_or_odd(2)

####################
# Convert a number to a string 
def number_to_string(num):
    #convert to string
    return str(num)

number_to_string(332)

################### 
# Count vowels 
def get_count(sentence):
    # store vowels in a string variable of type string (iterable)
    vowels = "aeiou"
    #set count to 0 initially
    count = 0
    #use a for loop to check each character in sentence
    for character in sentence:
        #if each lowercase character is found in "a", "e", "i", "o", or "u" add 1 to count
        if character.lower() in vowels:
            count+=1

    return count

print(get_count("I am a WOrd to count vowels."))