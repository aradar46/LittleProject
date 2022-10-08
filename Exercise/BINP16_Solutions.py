# -*- coding: utf-8 -*-
"""
Title: 1_Simple_data_type-exercise_solutions.py
Date: 2021-09-21
Author: Yali Zhang

Description:
    This script contains the codes and solutions of exercise for simple data type part.

Usage:
    In each code cell (between #%%), use 'Ctrl+Enter' to run solutions separately.
"""
#%%

# 1	Simple data type


## 1.1 Arithmetic

#%%
### 1
5/0 # ZeroDivisionError: division by zero
#%%
print(5//2) # 2
print(5%-2) # -1
print(-5%2) # 1
print(-5%-2) # -1
print(round(-3.6)) # -4
print(round(4.5)) # 4
print(round(5.5)) # 6 
print(round(6.615,2)) # 6.67
#%%
'''
NOTE:
1. round(): Take the nearest number. But for 0.5 take the nearest even number
2. The divisor "//" in Python returns the largest integer that is not greater than the real result
3. Remainder operator "%"
   a/b=c...d
     If a and b are both positive or negative, the result will be obtained according to the normal operation.
     If one of a and b is positive and one is negative, calculate the remainder according to d=a-b*[a//b].
   The running result of 5%-2 is -1, according to the formula, the result of 5//-2 is -3, and the remainder result is -1
'''

#%%
### 2
print(round(int(4.6))) # 4  int(4.6)=4
print(int(round(4.6))) # 5  round(4.6)=5

#%%
### 3
print(int(-3.1))# -3
from calendar import c
import math
from xml.dom.xmlbuilder import _DOMInputSourceStringDataType 
print(math.floor(-3.1)) # -4 returns the nearest integer less than the floating point number
print(math.floor(3.1)) # 3
print(math.ceil(3.1)) # 4

#%%
### 4
print(type(6.66)) # float
print(int(6.66)) # 6
print(float('6.66')) # 6.66
#%%
print(int('6.66')) # ValueError: invalid literal for int() with base 10: '6.66'
#%%
print(int(float('6.66')))
#%%

## 1.2 Strings

#%% 
### 1
print(len(5)) # TypeError: object of type 'int' has no len()

#%%
### 2
print(len(str(len('len')))) # 1 len('len')=3 str(3)='3' len('3')=1

#%%
### 3
#### a)
my_string = "ATGC"
my_string += 'XXX'
print(my_string) # my_string='ATGCXXX'
#%%
#### b)
my_string = "ATGC"
print(my_string*4) # ATGCATGCATGCATGC
#%%
#### c)
print(len(my_string*4))
#%%
#### d)
string = "AAAAGGAAAAGGAAAA"
print(string.find('GG')) # 4 .find just can find the position of the first obj.
#%%
#### e)
print(string.count('GG')) # 2
import re
print(re.search('GG', string)) # <re.Match object; span=(4, 6), match='GG'>
#%%
#### f)
print(string.count('AAAA')) # 3
print(string.count('AAA')) # 3 The overlap character is only counted once
print(string.count('AA')) # 6
print(string.count('A')) # 12
#%%
#### g)
v1 = 'AcgT' 
v2 = 'acGT'
print(v2.lower().find(v1.lower())) # also can use v.upper() to transfer all letters as the same format

#%%
### 4
#### a)
name = "Karl"
surname = "Johansson"
print("My name is {} {}".format(name,surname))
#%%
#### b)
name = "Karl"
surname = "Johansson"
print("My name is {0} {1}".format(name,surname))
#%%
#### c)
name = "Karl"
surname = "Johansson"
print("My name is {0}{0} {1}".format(name,surname))
#%%
#### d)
name = "Karl"
surname = "Johansson"
print("My name is {0} {1}".format(name,surname[0:5]))
#%%
'''
NOTE:
1. string formatting is useful when you want to add different variable into one line. It can be
   used into a loop in which the variable name doesn't change but value of this variable change.
2. \n \t can be used in format string part
3. operation can be used on the format variable
'''

#%%
### 5
seq_1 = 'AAATT '
seq_2 = 'CCCGG'
print(seq_1[0:-1] + seq_2)
print(seq_1.strip() + seq_2)

#%%
### 6*
import re
import sys
import random

nucleotide = ('a', 'c', 'g', 't')

oligo = input('Type a sequence: ')

# Test is the string the user types is valid
matchObject = re.match('[acgtACGT]{' + str(len(oligo)) + '}', oligo)
if not matchObject:
    print('Only characters a, c, g, t, A, C, G, T should be used', file = sys.stderr)
    sys.exit()

oligoLowercase = oligo.lower() # So we do the comparisons using only lowercase nucleotides

while True: # There is a 25% risk that we pick a nucleotide that the position already has

    randomPosition = random.randrange(len(oligo)) # Pick a random position
    indexNt = random.randrange(len(nucleotide)) # And the length is of course 4
    randomNucleotide = nucleotide[indexNt]

    if oligoLowercase[randomPosition] != randomNucleotide:
        # The oligo string is immutable so we print out two parts
        # that have not changed plus the mutated nucleotide
        print(oligoLowercase[:randomPosition] + randomNucleotide + \
              oligoLowercase[randomPosition + 1:])
        break # When we found a different nucleotide we break the while loop

for i in range(1,5):
    print(i)

#%% 

## 1.3 Numbers
 
#%%
### 1
for i in range(1,1001): # 1001 is exclusive
    if i % 3 == 0:
        print(i)

#%%
### 2
for i in range(3000,4001): # 4001 is exclusive
    if i % 3 == 0 and i % 5 != 0:     
        print(i)

#%%
### 3
userValue = int(input('Type a number: ')) # The number will be imported as a string so we cast it to an integer
if userValue == 1:
    print(1)
elif userValue == 2:
    print(1, '\n', 1, sep='')
else:
    print(1, '\n', 1, sep='')
    values = [1, 1] # the first two values in the list
    for i in range(userValue - 2):
        newValue = sum(values)
        print(newValue)
        values[0] = values[1] # renew the previous values for a new value
        values[1] = newValue

#%%
### 4
import sys
number = int(input('Type a number: ')) # The number will be imported as a string so we cast it to an integer

# Judge the input content, if it does not meet the set program will be terminated
if number == 0:
    print(1) # 0! = 1
    sys.exit() # To avoid an else statement
elif number < 0:
    print('The number can not be negative', file=sys.stderr)
    sys.exit() # To avoid an else statement

total = 1 # set a start number

for i in range(2, number + 1): # conclude input number into range 
    total *= i

print(total)

#%%
### 5*
# https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers

primeList = ['2'] # To be able to join in the last step the list must contain strings
currentValue = 3

while True:
    prime = True # We assume that the value we test is a prime

    # We only test a factor up to half of the number we investigate to save speed
    for i in range(3, int((currentValue + 1) / 2), 2):
        # If we find that the number dividable by a smaller number
        # it's not a prime and we break
        if currentValue % i == 0:
            prime = False
            break

    if prime is True:
        # To be able to join in the last step the list must contain strings
        primeList.append(str(currentValue))

    currentValue += 2 # We only test 3, 5, 7 and so on as the denominators to save speed

    if len(primeList) == 1000:
        print('\n'.join(primeList))
        break

#%%

#!Prime Numbers
#! #adrcodes

primeList = [2]      # this list will contain the prime numbers
current_value = 1    # we strat with the current value of 1, since we have 2 the only even pime value in our list 
while len(primeList)<101:  #this loop will continue untill we reach 100 prime numbers
    current_value += 2      
    for i in range(2,int((current_value+1)/2)): 
        if current_value % i == 0: 
            #// print(current_value, " / ", i , "=", int(current_value/i), "not a prime!")
            break
        # if current_value has a reminder for each i the loop breaks and while loop starts again
        # with new current_value. if current_value does not haave any reminder it will not activate
        # the break . so will go down into the else condition and will add to the prime list.
        # this happens untill the primelist lenghth reach 100 and while loop deactiveted.

    else:
        #//print(current_value, "is a prime")
        primeList.append(str(current_value))

print("Here, the primes: \n",primeList)    


#%%

#! factorial
#! #adrcodes

the_number = 5
the_total = 1
for i in range(2,the_number+1):
    the_total *= i

print(the_total)

# %%
#! Fibonacci series
#! #adrcodes
'''In a Fibonacci series, the new value of the series is the sum
of the previous two. It looks like this: 1, 1, 2, 3, 5, 8, 13, 21...
Ask the user for a number and print that many values from the Fibonacci
series.'''





#%%
#! #chapter2

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: Collection data types - answers.

This script contains answers for the Collections data types: Lists, Dictionaries
    and Sets.

These answers are only one possible solution for the problems, which may be
    solved in many different ways.

Some answers use loops, file handling and if statements. In this exercise,
    these concepts were still not introduced. So, feel free to come back to some
    of them after learning about these concepts. And remember, Google is your
    best friend.

Created on: 2021-09-22
Author: Arthur Boffelli Castro
"""

################################################################################
# Collection data types: Lists


#%% 1.
# Ask for the ingredients using the input function
ingredients = input("Please enter some ingredients (separated by spaces):\n")

# Split the string into a list. The default argument for the split function is
# whitespaces, so each ingredient will become a list item.
ingredients_list = ingredients.split()

# Insert bread in the beginning the list. The first argument in the insert
# function is the position and the second is the object to be inserted.
ingredients_list.insert(0, "bread")

# Use len to insert in the last position, independently of how many ingredients
# the user wrote.
ingredients_list.insert(len(ingredients_list), 'bread')

print(ingredients_list)


#%% 2.
print('='*50)  # Add a line to separate the result from each question
# Ask for numbers using the input function.
number_string = input("Please add some numbers separated with comma (,):\n")
# Split the string into a list using the comma as a delimiter.
number_list = number_string.split(",")

# Here an option without using loops, using the map function.
# Convert the map result into a list
integer_list = list(map(int, number_list))

# Print the sum of the list
print(sum(integer_list))


#%% 3.
print('='*50)
# Copy the line of codons.

# We can escape the new line with "\" to visualize better.
codons = "AAA AAT AAC aag ATA ATT ATC ATG Aca ACT ACC Acg AGA AGT AGC agG TAA \
TAT TAC TAG TTA TTT TTC TTG TCA tct TCC tCg TGA TGT TGC TGG CAA CAT CAC CAG \
CTA cTT ctc CTG CCA CCT CCc CCG CGA CGT CGC cgg GAA GAT GAC GAG GTa GTT GTC \
GTG GCA GCT GCC GcG GGA GGT GGC gGG"

# To fix the cases we must change it before turning it into a list, it is
# possible to stack codes. The codes will be ran in the sequence that they
# appear. In this case, first the string will become uppercase, then it will
# be split into a list.
codon_list = codons.upper().split(" ")
print(codon_list)


#%% 4.
print('='*50)

# Make a list with all codons that encode for Leucine.
leucine_codons = ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"]

# Remove each of them from the codon list
# We could remove one by one manually with .remove(), but let's use a loop to
# help us.
for codon in leucine_codons:
    codon_list.remove(codon)

print(codon_list)

#%% 5.
print('='*50)
# Using nested loops we can create all possible combinations of letters
bases = "ATCG"
codon_list = []

for base1 in bases:  # First letter in the codon
    for base2 in bases:  # Second letter in the codon
        for base3 in bases:  # Third letter in the codon
            # Add the three letters together and append to the list.
            codon_list.append(base1+base2+base3)

print(codon_list)


################################################################################
# Collection data types: Dictionaries

#%% 1.
print('='*50)
# Two ways of creating the dictionary
# (1) Create an empty dictionary and populate it
fruit_dict = dict()

# Add the key inside the [] and the values for that key. This will either create
# a new key, or overwrite an existing key.
fruit_dict["oranges"] = 2
fruit_dict["pears"] = 2
fruit_dict["apples"] = 4

print(fruit_dict)

# (2) Hard code a dictionary
# Keys and values are separated by ":"
fruit_dict = {"oranges": 2,
              "pears": 2,
              "apples": 4
              }
print(fruit_dict)


#%% a)
print('='*50)  # Add a line to separate the result from each question
# Update the values of the dictionary
# As arithmetic operation work for dictionary values, we can use += to update
# the value.
fruit_dict["pears"] += 2
# the result is the same as "fruit_dict["pears"] = fruit_dict["pears"] + 2"
fruit_dict["oranges"] += 5
fruit_dict["watermelons"] = 1

print(fruit_dict)


#%% b)
print('='*50)
# Iterate through the keys and print the value
for fruit in fruit_dict:
    # fruit is the key of the dictionary (any name can be chosen)
    # fruit_dict[fruit] retrieve the value of the key
    print(fruit + ":", fruit_dict[fruit], 'pieces')


#%% c)
print('='*50)
# Now we need to sort the fruits in alphabetical order.
# We can use the sorted function to sort the dictionary keys.
for fruit in sorted(fruit_dict):
    print(fruit + ":", fruit_dict[fruit], 'pieces')


#%% 2.
print('='*50)
# Create a new dictionary
friend_week_fruits = {'apples': 2, 'pears': 1, 'oranges': 2, 'waxberry': 4}
print(friend_week_fruits)

# Join the two dictionaries
# First we copy our fruit dict
joint_dict = fruit_dict

# Let's iterate in the friend's dict
for fruit in friend_week_fruits:
    # if the fruit is already present in the joint dict, just add the friend's
    # value
    if fruit in joint_dict:
        joint_dict[fruit] += friend_week_fruits[fruit]
    # if not, create a new key with the friend's value
    else:
        joint_dict[fruit] = friend_week_fruits[fruit]

# Print just like ex. 1-c.
for fruit in sorted(joint_dict):
    print(fruit + ":", joint_dict[fruit], 'pieces')


#%% 3.
print('='*50)
# The file can be created manually
# Here is one option of creating it through python
with open('tiny_tab.txt', 'w') as tiny_tab:
    tiny_tab.write('ProteinID\tProteinSeq\n'
                   'prot1\tAGSATGDASD\n'
                   'prot4\tASLWASLD\n'
                   'prot9\tPPASDSADSAD\n'
                   'prot2\tXXSWKJXS\n'
                   'prot8\tPSOASSADASD')


#%% a)
# Create a protein dictionary using the file we created
tiny_tab = 'tiny_tab.txt'

# Start an empty dictionary
prot_dict = {}

# Open the file
with open(tiny_tab, 'r') as tiny_tab:
    for line in tiny_tab:
        # Python is case sensitive, so if we use startswith("prot") the header
        # will be excluded
        if line.startswith("prot"):
            line = line.split('\t')  # Split the line in the tabs
            prot = line[0]  # protein name is the first object
            seq = line[1].strip()  # sequence is the second object
            # strip removes the new line

            # Add the prot as key and seq as value in our dictionary
            prot_dict[prot] = seq

# Print the result
for prot in prot_dict:
    print(prot + ':', prot_dict[prot])


#%% b)
print('='*50)
# Print only sequences that contain Tryptophan (W)
for key in prot_dict:
    # check if W is present in the value(remember that python is case sensitive)
    if 'W' in prot_dict[key]:
        # If yes, print it
        print('{}: {}'.format(key, prot_dict[key]))


#%% c)
print('='*50)
# Do not print sequences that contain X
for key in prot_dict:
    # Check if X is NOT present in the sequence.
    if 'X' not in prot_dict[key]:
        # If X is not present, print it
        print('{}: {}'.format(key, prot_dict[key]))


################################################################################
# Collection data types: Sets.


#%% 1.
print('='*50)
# Path to the file
# If the file is not in the same directory of the script, add the path
regions_fna = 'regions.fna'

# Initialize a counter, starting from 0.
count = 0
# Initialize an empty set, sets prevent duplicates.
reg_set = set()

# Open the file using the absolute path variable, and "r" for readable
# (we only want to read the file, not edit it)
# Try to use with open() to prevent not closing the file, this function closes
# closes automatically when it's done.
with open(regions_fna, "r") as I1:

    # as I1, meaning that I1 is the variable we have for the file.
    for line in I1:  # Iterates through all lines in I1

        # Checks if the first character in the line is ">", so we only get
        # the lines with the sequence ID's
        if line.startswith(">"):

            # Observing the file, we can see that the ID is separated with a
            # space from the rest of the information in the line
            # So use split to separate the information in a list.
            line = line.split(" ")

            # Take the first item in the list (where the sequence ID is found)
            ID = line[0]
            reg_set.add(ID)  # Add to the set
            count += 1  # 1 is added to count.

# 1 is added to count every time an ID is added to the set,
# even if it is a duplicate. That gives us how many IDs we have in total.
# Sets store only unique objects, so if we count the length of our set, we
# have the number of unique IDs.

print("Sequences found: {}\nUnique sequences: {}".format(count, len(reg_set)))


#%% 2.
print('='*50)  # Add a line to separate the result from each question
reads_fna = 'reads.fna'
reads_ids = 'reads_ids.txt'

# Initialize an empty set and an empty list (for comparison of time)
id_set = set()
id_list = []

# Open the files, more than one file can be opened in the same line
with open(reads_ids, 'r') as I1, open(reads_fna, 'r') as I2:
    for line in I1:  # Parse through the first file (reads_ids)
        id_line = line.strip()  # Remove the linebreak and spaces
        id_set.add(id_line)  # Add the sequence to the id_set.
        id_list.append(id_line)  # Add the sequence to the id_list

    count = 0  # Initialize a counter for each time a sequence ID from reads_ids
    for line in I2:  # is found in the .fna file.
        if line.startswith('>'):  # Checks if the line starts with >
            line = line.split(" ")  # Splits the line into a list
            # Take only the first object in the list (id)
            id_line = line[0][1:]
            # The slicing command [1:] removes the ">" from the first position
            if id_line in id_set:  # Checks if the ID_line exists in the set.
                #if id_line in id_list:  # Compare using the list.
                count += 1  # Adds one to the counter.

print(count, "ids are in the fasta file")


#%% 3.
print('='*50)
# File paths in variables
regions_sub1 = 'regions_sub1.fna'
regions_sub2 = 'regions_sub2.fna'
regions_sub3 = 'regions_sub3.fna'

# Initiate empty sets for all files
sub1_set = set()
sub2_set = set()
sub3_set = set()

# Open the files to populate the sets
with open(regions_sub1, 'r') as I1, open(regions_sub2, 'r') as I2, open(regions_sub3) as I3:

    for line in I1:  # regions_sub1
        if line.startswith(">"):  # Check if line starts with >
            line = line.split(" ")  # Split the line in spaces
            # Take the first item of the line (except > with the slicing [1:])
            ID = line[0][1:]
            sub1_set.add(ID)  # Add the ID to the sub1 set.

    for line in I2:  # regions_sub2
        if line.startswith(">"):
            line = line.split(" ")
            ID = line[0][1:]
            sub2_set.add(ID)  # Add IDs to sub2 set

    for line in I3:  # regions_sub3
        if line.startswith(">"):
            line = line.split(" ")
            ID = line[0][1:]
            sub3_set.add(ID)  # Add IDs to sub3 set

# Using intersection (&) in sets, only the values that are present in both will
# remain
intersection_1_2 = sub1_set & sub2_set
# The length of the set will tell us the number of ids.
print(len(intersection_1_2), "ids are present in both sub1 and sub2")

# Now let's remove the ones present in sub3 subtracting the set sub3.
no_sub3 = intersection_1_2 - sub3_set
# The length of the set will tell us the number of ids.
print(len(no_sub3),
      "ids are present in both sub1 and sub2, and not present in sub3")


#%%
#! chapter3
#!/usr/bin/env python3
"""
Created on Thu Sep 23 16:21:23 2021

@author: Mara (credit for some solutions goes to Malou)
"""
################## Program control and logic ########################
""" This script contains solution suggestions for the lesson on "Program control and logic". These solutions are only suggestions and there may exist many different solutions for the same problem."""
#####################################################################

#%% 1. Create a script that greets the user based on their name (special greeting if it is your name).

my_name = "Malou"               # Let the program know my name
users_name = input("What is your name? ") # Ask the current user their name

if users_name == my_name:       # Checks if the input name is identical to the my_name variable (note that the names are case sensitive)
    print("So very nice to see you {}!".format(users_name))    # Special greeting and the users_name is printed using the format function
else:                           # If users_name and my_name are not the same, another greeting is printed
    print("Hi {}.".format(users_name))


#%% 2. Modify the previous script to give a special greeting for your friends

my_name = "Malou"                                 # First create a variable with my name
friends_names = ["Eran", "Anna", "Dag"]           # List of my friends' names
users_name = input("What is your name? ")         # Ask the current user their name

if users_name == my_name:                         # Checks if users_name is identical to my_name (case-sensitive)
    print("So very nice to see you {}!".format(users_name)) # Printing the special greeting and the input name, using the format funtion
elif users_name in friends_names:                 # Checks if users_name is found in the friends list 
    print("What's up, {}?".format(users_name))    # If True, a special friend greeting is printed together with the name
else:
    print("Hi {}.".format(users_name))            # If the use is neither you, nor your friend, a regular greeting is used


#%% 3. FizzBuzz simplified

current_value = int(input("Please enter a number: ")) # Input will allow the user to give an answer to the question, which will be the value assigned to the variable
# The int function will directly convert the input to an integer. This will only work if the input is a number, without any other characters.
if current_value%3 == 0:    # If current_value modulo 3 is 0 (if the number is divisible by 3)
    fizz = "Fizz"           # A fizz variable will be assigned with the string "Fizz"
else:
    fizz = ""               # If it is not, the same variable will be assigned an empty string instead
if current_value%5 == 0:    # If current value modulo 5 is 0 (if the number is divisible by 5)
    buzz = "Buzz"           # A variable buzz will be created and assigned the string "Buzz"
else:
    buzz = ""               # Else, the same variable will be assigned an empty string.

print("{}{}".format(fizz,buzz) or current_value) # This will print the current_value only if the string is empty. If the string is not empty, it will print the string, which will either be Fizz, Buzz or both, depending on the current_value.


#%% 3. FizzBuzz simplified - another possible solution (using elif)

current_value = int(input("Please enter a number: ")) # Input will allow the user to give an answer to the question, which will be the value assigned to the variable
# The int function will directly convert the input to an integer. This will only work if the input is a number, without any other characters.

if current_value%3 == 0 and current_value%5 == 0: # If current_value modulo 3 is 0 and current_value modulo 5 is 0 (the number is divisible by both 3 and 5)
    print("FizzBuzz")       # Print the corresponding message
elif current_value%3 == 0:  # If current_value modulo 3 is 0 (the number is divisible by 3)
    print("Fizz")           # Print the corresponding message
elif current_value%5 == 0:  # If current_value modulo 5 is 0 (the number is divisible by 5)
    print("Buzz")           # Print the corresponding message
else:                       # If the number is neither divisible by 3 nor 5
    print(current_value)    # Print the number itself


#%% 4. Real FizzBuzz. Make the FizzBuzz script run over all of the integers from 1 to 100.

# The same script as in task 3, but iterating over 100 numbers.

for num in range(1,101):        # Iterates through all numbers from 1 to 100 (101 is not included)
    
    if num%3 == 0:              # If the number is divisible by 3
        fizz = "Fizz"           # A fizz variable will be assigned with the string "Fizz"
    else:
        fizz = ""               # If it is not, the same variable will be assigned an empty string instead
    if num%5 == 0:              # If the number is divisible by 5
        buzz = "Buzz"           # A variable buzz will be created and assigned the string "Buzz"
    else:
        buzz = ""               # Else, the same variable will be assigned an empty string
    print("{}{}".format(fizz,buzz) or num)            # This will print the number only if the string is empty. If the string is not empty, it will print the string, which will either be Fizz or Buzz or both, depending on the number.


#%% 4. Real FizzBuzz - alternative solution (using elif)

for num in range(1, 101): # Iterates through all numbers from 1 to 100 (101 is not included)

    if num%3 == 0 and num%5 == 0: # If the number is divisible by both 3 and 5
        print("FizzBuzz")         # Print the corresponding message
    elif num%3 == 0:              # If the number is divisible by 3
        print("Fizz")             # Print the corresponding message
    elif num%5 == 0:              # If the number is divisible by 5
        print("Buzz")             # Print the corresponding message
    else:                         # If the number is neither divisible by 3 nor 5
        print(num)                # Print the number itself


#%% 5. Calculate the scores for a golf course, knowing the hole number and the number of strokes

par_list = [4,3,5,2,5,4,7,6]        # List of pars for all the holes

hole = int(input("What hole are you on? (1-8) ")) # Ask user about hole number and store it in the hole variable
strokes = int(input("How many strokes? ")) # Ask user about number of strokes and store it in the strokes variable
# int converts the numeric input given by the user into an integer

par = par_list[hole-1]              # For each hole, the index in the par_list of that hole's par is smaller by 1 than the number of the hole (hole number 1 corresponds to index 0 of the list)
difference = strokes-par            # The difference used to calculate the score is the number of strokes minus the par

# Depending on the difference between the number of strokes and the par, different score names are assigned to a new variable called score
if difference <= -3:
    score = "Albatross"
elif difference == -2:
    score = "Eagle"
elif difference == -1:
    score = "Birdie"
elif difference == 0:
    score = "Par"
elif difference == 1:
    score = "Boogie"
else:                               # Else covers the situations when the difference is larger or equal to 2
    score = "Double boogie"

print("Your score is: {}".format(score)) # The name corresponding to the score is printed using the format function and the value assigned to the score variable


#%% 6. Print the uppercase version of every second letter in a list, starting from the first

letter_list = ["a", "b", "c", "e", "f", "g", "h", "i"] # The list of letters that is given

for index, letter in enumerate(letter_list): # The for loop iterates through all of the items of the list. By using enumerate, for each item the index and the value (the letter in this case) are stored in two separate variables
    if index%2 == 0: # We are interested in every second letter, starting with the first. The first letter has the index 0. The other ones will have even numbers as indexes. Therefore, we are only looking at those items that have indexes divisible by 2
        print(letter.upper()) # Print those letters as their uppercase version


#%% 7. Find out which codons from an mRNA sequence encode tyrosine

sequence = "UAUAAACGAUACCAUUACUAUGACCAUGGG" # The mRNA sequence consisting of 10 codons
encoding_tyr = ["UAU", "UAC"]   # List of the codons known to encode tyrosine

# In order to keep track of the separate codons and their order, we separate the mRNA sequence into codons and add them to a list.
# We use a sliding window of indexes to store strings of 3 nucleotides at a time into a list
pos_1 = 0                       # Begin reading the first codon at index 0
pos_2 = 3                       # The end of the first codon is at index 3 (not inclusive)

codons = []                     # Empty list to store the codons

while pos_1 <= len(sequence)-3 and pos_2 <= len(sequence): # We want to keep moving the sliding window accross the sequence until the beginning of the last codon is 2 positions away from the end of the string (3 less than the length of the string)
# The end of the final codon will be equal to the length of the sequence (the final nucleotide is at index 29, but we need to read until index 30 in order to include the final position)
    codons.append(sequence[pos_1:pos_2]) # Append the substring between the two positions to the list of codons
    pos_1 = pos_1 + 3           # Move the sliding window 3 steps forward, to read the next codon
    pos_2 = pos_2 + 3

for index, codon in enumerate(codons, start=1): # Iterate through the list of codons and store the index for each one. The argument start=1 allows the index numbering to begin at 1 instead of 0
    if codon in encoding_tyr:   # When finding a codon that encodes tyrosine
        print(index, codon)     # Print the number of that codon and the codon itself


#%% 8. Print the first 1000 prime numbers

primes_list = [2]               # Begin the list with the number 2

current_number = 3              # The first number to analyze is 3

while len(primes_list) < 1000:  # Keep adding prime numbers to the list until it has 1000 items. We use <1000 and not <=1000 because the final iteration of the loop begins when the list contains 999 numbers, and finishes with the 1000th prime number being added
# An easy way to check if a number is prime is to try dividing it by all of the prime numbers smaller than half of its value
    for i in primes_list:       # Prime numbers smaller than the current_number are already stored in the list. We want to try to divide the current_number by them
        if i <= (current_number+1)/2: # For efficiency, we are only trying to divide by the numbers smaller than half of the current_number
            if current_number%i == 0: # If a divisor is found, the loop breaks and the next current_number is tried
                break
    else:                             # When the current_number does not have any divisors from the list
        primes_list.append(current_number) # We add the number to the list of primes
    current_number = current_number + 2 # To test the next current_number, we increase it by 2. For efficiency, we are only testing the odd numbers

primes_string_list = [str(j) for j in primes_list] # primes_list contains integers. We convert them to strings to be able to display them in a nice way
# This command takes each element from primes_list, converts it into a string, and adds it to primes_string_list

print("\n".join(primes_string_list)) # Finally, print the 1000 prime numbers, delimited by a new line


#%% 9. Ask user for DNA sequence and raise an exception if any non-nucleotide letters are in the sequence

sequence = input("Please type a DNA sequence: ")    # Store the DNA sequence input by the user into the sequence variable
valid_nucleotides = ["A", "C", "G", "T"]            # List of valid nucleotides. The sequence should only contain these

for nucleotide in sequence:                         # Iterate through all of the nucleotides in the sequence
    if nucleotide.upper() not in valid_nucleotides: # To account for lowercase characters, convert the nucleotide being read into the uppercase version and check if it is found in the valid_nucleotides list. If it is not in the list...
        raise Exception("Your sequence contins an invalid nucleotide") # Raise an exception informing the user


#%% 10. Modify the previous script to ask for a DNA sequence until a valid one is entered

valid_nucleotides = ["A", "C", "G", "T"] # List of valid nucleotides

while True:                              # Begin the loop that ends when a valid sequence has been entered
    try:                                 # Use try to identify and correct any errors
        sequence = input("Please type a DNA sequence: ") # Ask the user to input the sequence
        for nucleotide in sequence:      # If there are any non-nucleotide characters in the sequence, raise an exception (see exercise 9 for more details about this loop)
            if nucleotide.upper() not in valid_nucleotides:
                raise Exception("Your sequence contains an invalid nucleotide")
        break                            # The loop ends if no exceptions are raised
    except Exception:                    # When an exception is raised, ask the user to re-enter a sequence
        print("Your sequence contins an invalid nucleotide. Please try again.")

print("You have entered a valid DNA sequence.") # When a correct sequence is input, the loop ends and this message is printed



#%%
#! #chapter4

"""
@author: Mattis Knulst

Question: 1. Python natively supports using file addresses with forward slashes on any system, but there are
cases where you need to do things to those paths where string manipulation just becomes a hassle. This is
especially true if you want to make your scripts work with paths in different operating systems. Windows infamously
uses backslashes for its own paths and if you write a script for a friend or colleague they may just want to paste
a path into the command line. You may also be interested in listing files, directories or going up and down file trees.
The module for this used to be os, but there is a newer module in the standard library that is extremely powerful
for working with paths on any OS: pathlib.Path

a) import Path from pathlib
hint: almost the same as the above line, but Python syntax demands different order!
b) Store your current working directory and home directory in variables and print them, also print their type().
hint: start by typing Path and scroll through the different methods or look in the docs for pathlib!
c) make a new directory by joining the string "new_dir" with the parent of your working directory
hint: you need Path.parent, Path.joinpath() and Path.mkdir()
d) List all directories in your home directory that contain a letter that you choose! Print these to screen!
hint: use Path.glob()
e) Use the same method as in d) but this time only extract file paths matching a pattern and print only the file name,
excluding the path and file extension, along with it's type!
hint: Path.stem and Path.is_file() will be useful here!
f) make your own Path object from a string, the path may or may not exist, use pathlib to check if it does and
print a nice message that let's the user know!
hint: use Path() and Path.exists()
"""
# a)
from pathlib import Path
#%% b)
my_wdir = Path.cwd()
my_home = Path.home()
print(f"My home directory is {my_home} and my current working directory is {my_wdir}\n"
      f"Their types are:\t {type(my_wdir)} and {type(my_home)}")
#%% c)
my_wdir.parent.joinpath("new_dir").mkdir(exist_ok=True)
# you can also remove this:
# my_wdir.parent.joinpath("new_dir").rmdir()
#%% d) looking for paths with l in them
for p in my_home.glob('*l*'):
    print(f'Found the path: {p}')
#%% e)
# think of list comprehensions every time you may want to use a filter!
for my_path in [p.stem for p in my_home.glob('*l*') if p.is_file()]:
    print(my_path, ' is of the type: ', type(my_path))

#%% f)
a_path = Path("this/is/a/bs/path")
if a_path.exists():
    print(f"{a_path} exists!")
else:
    print(f"{a_path} cannot be found!")
########################################################################################################################
"""
@author Mattis Knulst
Question 2: As a bioinformatician you are guaranteed to encounter many file formats. Generally the files you encounter
will be of one of two types. They can be text files, or binary. Text files are easy to read and parse in Python as long
as they use an encoding that Python can recognize. Binary files can generally only be read with libraries that unpack
the information and make it accessible in your programming language. Fasta/q files are required by GenBank to be ASCII
encoded.
a) Save the string "är det du som har kaffebrödet, Gösta?" to a variable, then use the string method str.encode()
to make a new variable that is ASCII encoded. Print both.
"""
#%%
my_string = "är det du som har kaffebrödet, Gösta?"
ascii_string = my_string.encode(encoding="ascii", errors="ignore")
print(f"{my_string} \n {ascii_string}")
"""
b) In the above example you should get either an error message or, if you ignore errors you'll see a slightly
different string than you may have expected. These are the kind of shenanigans encoding can cause. Beyond encoding,
text files also tend to have a format, which is documented. In a scientific setting you will see a lot of CSV tables.
The CSV format is a table where every column is separated by a comma, but sometimes by other separators such as
semicolon. Create a simple CSV table and write it to a file. Have at least one column
with integer or float values.
"""
#%%
my_table_dict = {
    "Name": ["Vi", "Julio", "Mara", "Mattis"],
    "Role": ["TA","TA","TA","TA"],
    "Space invaders High Score": [91000, 64000, 15000, 1000000],
}
# it is acceptable to use the csv builtin module to do this or pandas if you know how/want to know!
# open file in write mode!
with open("data/out.csv", 'w') as out:
    # get the keys, returned as list, join list elements with comma, print to file
    print(','.join(my_table_dict.keys()), file=out)
    for i, value in enumerate(my_table_dict['Name']):
        # print csv row by row and separate by comma, to file
        print(f"{value},{my_table_dict['Role'][i]},{my_table_dict['Space invaders High Score'][i]}", file=out)

"""
c) Reading and cleaning up CSV files is a huge topic, but will be elaborated on in later courses. For the future
remember that you will probably want to install Pandas when you are working with CSV files. Instructions for Pandas
are in the extended exercise document. Your school computer should have conda installed, otherwise follow the suitable
instructions at https://conda.io/projects/conda/en/latest/user-guide/getting-started.html once you have set up conda
you can use anaconda-navigator or the CLI tool: conda install pandas
Read your csv file, then find the mean, median, max and min values for your numerical column and print them!
"""
#%%
import pandas as pd
# it is of course fine if you use other methods!
my_table = pd.read_csv("data/out.csv")
# look at what your table contains
my_table.info()
# long column names, especially with spaces should be avoided!
# in your own example use something like col_1, col_2...
my_mean = my_table['Space invaders High Score'].mean()
my_median = my_table['Space invaders High Score'].median()
my_max  = my_table['Space invaders High Score'].max()
my_min = my_table['Space invaders High Score'].min()
print(f"Mean high score: {my_mean}\n"
      f"Median high score: {my_median}\n"
      f"Minimum high score: {my_min}\n"
      f"Maximum high score: {my_max}\n"
      # bonus, extract the entire row with the highest value
      f"{my_table.loc[my_table['Space invaders High Score'].idxmax()]}")

########################################################################################################################
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:48:56 2020

@author: malou
"""

##############################################################################
# %% 3. Create a script that runs from the terminal with input file and output file as arguments.
########### Importing packages and assigning variables #######################

import sys
# check the that we have exactly 3 arguments
if sys.argv == 3 and Path(sys.argv[1]).is_file():
# sys.argv[1] is path to the input file (paxillus.fna) you write in the terminal when running the script.
    infile = sys.argv[1]
# this is the second argument you pass in the terminal (parse_output.fna), which here will be the outfile.
    outfile = sys.argv[2]
# The outfile don't have to exist, it will be created when the file is open as writeable "w".
else:
    # you'll have to edit these to something that makes sense!
    infile = "data/reads.fna"
    outfile = "data/out.fa"

# Opens both the infile (readable "r") and outfile (writeable "w"), with the new variable names in_1 and out_1.
with open(infile, "r") as in_1, open(outfile, "w") as out_1:
    for line in in_1:  # Parses through the lines in the infile
        if line.startswith(">"):  # Checks if line starts with > (ID lines start with >)
            line = line.split(" ")  # Splits the line with respect to space
 # Takes the first element of the line (using index [0]), and at the same time exclude the first letter ">" with the indexing [1:]
            ID = line[0][1:]
            print(ID, file=out_1)  # Prints the ID to the outfile.

# Example for not using the "with" function.
# run previous section with edited paths to get variables for infile and outfile!
# in your own script these should come from sys.argv!
in_1 = open(infile, "r")  # Opens the files directly
out_1 = open(outfile, "w")

for line in in_1:  # Parses through the lines in the infile
    if line.startswith(">"):  # Checks if line starts with > (ID lines start with >)
        line = line.split(" ")  # Splits the line with respect to space
        ID = line[0][
             1:]  # Takes the first element of the line (using index [0]), and at the same time exclude the first letter ">" with the indexing [1:]
        print(ID, file=out_1)  # Prints the ID to the file O1.

in_1.close()  # When not using the with function to open files, they need to be closed after their use.
out_1.close()
"""
Open files that have not been closed can result in errors e.g. when trying to delete the file!
"""

# %% 4. Parse through paxillus.fna, calculate GC content for each sequence, create a new file with the ID's and GC
# percent. check if the script was executed from command line with two arguments and if the first arg is a file!
if len(sys.argv) == 3 and Path(sys.argv[1]).is_file():
    in_file = sys.argv[1]
    outfile = sys.argv[2]
else:
    in_file = "data/reads.fna"
    outfile = "data/out.fa"
# Opens both the in_file (readable "r") and outfile (writeable "w") at the same time, to be able to print in the outfile
# at the same time as parsing through the in_file, instead of open them separately and parse through the in_file twice
with open(in_file, "r") as in_1, open(outfile, "w") as out_1:
    for line in in_1:  # Parse through lines in the in_file,
        if line.startswith(">"):  # Checks if line starts with > (ID lines start with >).

            IDline = line.rstrip()  # rstrip will remove the linebreak at the end of the line.
            # next(I1) will skip to the next line in the file I1
            # (which in this case is the sequence belonging to the current ID)
            Sequence = next(in_1)
            Sequence = Sequence.rstrip()  # Removes the linebreak at the end of the sequence line.
            Sequence = Sequence.upper()  # Makes all letters upper case, in some files upper and lower case are mixed.

            seq_len = len(Sequence)  # Calculates the number of nucleotides in the sequence (length of the string)
            GCs = Sequence.count("G") + Sequence.count("C")  # Counts the G's and the C's and adds the values together.
            GC_content = GCs / seq_len  # Calculates the GC content
            # Print IDline + whitespace + GC_content * 100 rounded down to 2 decimals + %-sign + newline
            # sequence
            # notice that print() will automatically print to a new line for each iteration!
            print(f"{IDline} {round(GC_content * 100, 2)}%\n{Sequence}", file=out_1)
            # the above code may be easier to read if it is written as:
            # print(f'{IDline} GC:{GC_content*100}')


#######################################################################################################################
#%% Question 5
#!/usr/bin/env python3
# note that the above line lets you make the script executable on a Linux system
# a Windows system where Python is installed and added to PATH will attempt to run any script ending with .py
# with the Python interpreter
"""
@author: Mattis Knulst

Question:
Write a program that takes a fasta file as first argument and a sequence
ID as second argument. Search for the sequence ID in the file and print
the line number of the sequence. If it is not contained in the file, print
an informative error message.
"""
# Strategy:
# 1. we know that we need to deal with arguments from the command line
# 2. we are dealing with a text file with a specific format, so we should try to understand that format well
# 3. We want the line number of the sequence, which is the line after the header (and usually on several lines)

# sys and re are Standard library modules, you will be able to import these without installing any additional
# packages in the environment where you are using Python
import sys
# RegEx is an underrated tool, which can let us use general patterns that are more widely applicable
import re

# when developing a script with CLI args it may get tedious to always run the script with args
# if you are working in an IDE where you can just run a script with a shortcut while writing the code
# to make life easier, you can check for args and if there aren't any, you can just set the variables to some defaults

if len(sys.argv) == 3 and Path(sys.argv[1]).is_file():
    # we need to take a file path
    in_file = sys.argv[1]
    # then store a sequence ID
    seq_id = sys.argv[2]

else:
    # replace with valid paths
    in_file = 'data/reads.fna'  # prefer to use forward slash in paths, even on Windows!
    seq_id = 'HD257BI02IODST'
# out of interest, we may want to know what sys.argv is:

print(f'sys.argv is actually a {type(sys.argv)}\n'
      f'it contains this: \n{sys.argv}\n'
      f'which is why it is this many items long: {len(sys.argv)}\n')
# next we need to open the fasta file

with open(in_file, 'r') as my_in:
    # let's make a boolean variable to track whether we found anything
    # this will just remain false until we get a hit
    found = False

    # we need a pattern:
    # we expect that the person who will use this script does NOT know regex
    # but we can easily use re.escape to make sure whatever is handed from the CLI
    # is treated as a literal character
    # fasta headers are varied, sometimes they are whitespace separated, sometimes separated with | and so on
    # IDs mostly consist of word characters and dots (.), so let's look for a match that ends in something that is
    # not a dot or a word character

    pattern = re.compile(re.escape(seq_id) + r'[^\.\w]')
    # enumerate will return an index number and the corresponding line in the file for every iteration
    # this keeps your code short and snappy
    # note that the two now need to be 'unpacked' by declaring both variables separated by a comma

    for line_nr, line in enumerate(my_in):
        # if it is a header (starts with >), and we find the pattern, print the line number
        # one common error with 'and' in conditionals is that one statement will always evaluate to True/False
        # therefore it can make sense to start off with a nested if and then move the statements to one line
        # when you have tested that both ifs do what you want them to
        if line.startswith('>') and re.search(pattern=pattern, string=line):
            print(f'Sequence with the ID: {seq_id} found at line # {line_nr + 2}')  # computers start counting from 0
            found = True
# one of the great strengths of Python is that we can emulate natural language with statements like this!
if not found:
    print("Error: ID not present in the fasta file!")
# it can be good to make it very clear to the user that the program is now done with everything
print('Search complete, exiting...')
#######################################################################################################################
#%% Question 6
# !/usr/bin/env python3

import sys
from pathlib import Path

if len(sys.argv) == 3 and Path(sys.argv[1]).is_file():
    # use sys.argv when there are args
    infile = Path(sys.argv[1])
    outfile = Path(sys.argv[2])

else:
    infile = Path("data/sample.fastq")
    outfile = Path("data/out.fa")

# count variable declaration
i = 0
with open(infile, 'r') as fin, open(outfile, 'w') as fout:
    # this could be solved using enumerate, but this solution is also valid
    # and some may prefer it
    for line in fin:
        i += 1
        line = line.rstrip()
        if i % 4 == 1:
            line = line.replace('@', '>', 1)  # Only replace first occurrence
            print(line, file=fout)
        elif i % 4 == 2:
            print(line, file=fout)
