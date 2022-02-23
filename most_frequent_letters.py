print("============= PROGRAM FOR PRINTING THE LETTERS IN DECREASING FREQUENCY ======================")
from collections import Counter

input_string = input('Please enter a string :  ')

frequency_per_char = Counter(input_string)

#  Output
print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequency_per_char)))
