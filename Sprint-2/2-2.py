"""
Numbers in the Morse code have the following pattern:

all digits consist of 5 characters;
the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
starting with the number 6, each dot is replaced by a dash and vise versa.
Write the function morse_number() for encryption of a number in a three-digit format in Morse code.



Attention!
Do not use any collection data like lists, tuples, dictionaries for holding Morse codes
"""
def morse_number(str):
    result = ""
    for i in str:
        i = int(i)
        if i <= 5:
            morse = ("." * i).ljust(5, "_")
        else:
            morse = ("_" * (i - 5)).ljust(5, ".")
        result = result + " " + morse
    return result[1:]


print(morse_number("295"))
#result ..--- ----. .....
print(morse_number("005"))
#result ----- ----- .....
print(morse_number("513"))
#result ..... .---- ...--
print(morse_number("784"))
#result --... ---.. ....-