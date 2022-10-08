
# # my_string = "ATGC"
# # your_string = "xxx"

# # #our_string = my_string+your_string
# # our_string = "%s%s" %(my_string,your_string)
# # print(my_string+your_string)
# # print(our_string)

# # my_string=my_string*3
# # print(len(my_string))

# second_string = "AAAAGGAAAAGGAAAAGG"
# # print(len(second_string))
# # fist_GG = second_string.find('GG',0,16)
# # print(fist_GG)

# all_GG = []
# all_GG_list = list(second_string)
# print(all_GG_list)

# for i in range(1,17):
#     xc1 = all_GG_list[i]
#     xc2 = all_GG_list[i+1]
#     if xc1 == "G" and xc2 == "G":
#         all_GG.append(i)

# print(all_GG)


# one = "AcgT"
# two = "acGT"

# one_ =tuple(one.upper())
# print(one_)
# two_ = list(two.upper())
# for i in range(0,4):
#     print (one_[i] in two_[i])

"""
name = "Karl"
surname = "Johansson"
print("My name is " + name + " " + surname)
print("my name is {}%s {}".format("karl", "john") % (name))


seq_1 = 'AAATT '  # There is a space at the end of the nucleotide sequence
seq_2 = 'CCCGG'
seq_3 = seq_1 + seq_2
print(
    (seq_3.replace(" ", "")),
    (''.join(seq_3.split()))
)
print(seq_3.split()) """


from textwrap import wrap
import re
from curses import pair_number
from platform import freedesktop_os_release
import random
from turtle import position
from typing import Dict

# user_seq = input('Enter your seq:')
# length = len(user_seq) #lenghth of seq
# position_to_mutate = random.randint(0,(int(length)-1)) # selecting a position for mutation

# neclotidle_list = ["A", "T", "C", "G"] # neclotide list which will be shuffled in next line
# random.shuffle(neclotidle_list)

# list_user_seq = list(user_seq) #converting input to list for accessing items by position

# if list_user_seq[position_to_mutate]== "A":
#     list_user_seq[position_to_mutate] = neclotidle_list[1] # return a item 1 of randomize necleotide list to list_user_seq
# elif list_user_seq[position_to_mutate] == "T":
#     list_user_seq[position_to_mutate] = neclotidle_list[1]
# elif list_user_seq[position_to_mutate] == "C":
#     list_user_seq[position_to_mutate] = neclotidle_list[1]
# elif list_user_seq[position_to_mutate] == 'G':
#     list_user_seq[position_to_mutate] = neclotidle_list[1]

# mutated = "".join(list_user_seq) #converting list to concatenated string seq

# print("Orginal seq is %s\nmutated seq is %s ." %(user_seq,mutated))
# print("The position", position_to_mutate," is mutated to ", neclotidle_list[1])


# #take sequence from user
# sequence = input("Please write your sequence here:")
# #choose a random index from the input string
# random_index = random.randrange(0, len(sequence))
# #new sequence is old sequence which one character is randomly replaced by a random character between ACTG
# #string before teh index + index + string after index
# # : before the last braket means until the end of string
# mutate_sequence = sequence[:random_index] + random.choice('ATCG') + sequence[random_index+1:]
# print(mutate_sequence)
# print("The mutation is happend in place", random_index+1)


# listof3 =[]
# for i in range(3000,4000):
#     if i%3==0 and i%5!=0:
#            listof3.append(i)
# print (listof3)


# # Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto", nterms, ":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1


# Ask the user for a number and print the factorial. The factorial of 4
# (denoted 4!) is 1*2*3*4=24. What is the largest value a user can enter (on
# your computer)?

# factorial_user = int(input("which factoral? "))

# n1 = factorial_user
# n2= n1-1
# n3 = 1
# while n2>0:
#     n4 =n3*n1*n2
#     n1 = n1-2
#     n2 = n1-1
#     n3=n4
#     if n2<1:
#         print (n4)

# Python code to demonstrate naive method
# to compute factorial
# n = int(input("which factoral? "))
# fact = 1

# for i in range(1, n+1):
#     fact = fact*i


# print("The factorial of ", n, " is : ", end="")
# print(fact)


# # prime numbers
# primeList = []
# numPrime = len(primeList)
# if numPrime < 5:
#     for i in range(2, 44):
#         for u in (1,i-1):
#             if (i % u) != 0:
#                 None
#             else:
#                 print(i)
#                 primeList.append(i)

# print(primeList)


# 2. Collection data types: Lists, Sets and Dictionaries
# 2.1. Lists

# -------------------------------------
# 1. Ask the user for three ingredients, one after the other, and print a list with
# the ingredients surrounded by bread: [‘bread’, ‘ingredient1’, ‘ingredient2’,
# ‘ingredient3’, ‘bread’]

# ing1 = input("what 1")
# ing2 = input("what 2")
# ing3 = input("what 3")
# listA = ["bread", ing1, ing2, ing3, 'bread']
# print(listA)

# -----------------------------------------
# 2. Use input() to get a sequence of numbers (divided by comma). Calculate
# the sum and print it to standard output.

# num_seq = input("divided by comma")
# print(num_seq)
# list_seq= list(num_seq)
# no_cama_list = (list_seq[0::2])
# print (no_cama_list)

# for i in range(len(no_cama_list)):
#     no_cama_list[i] = int(no_cama_list[i])

# print (sum(no_cama_list))

# ----------------------------------------------
# 3. The line below contains all possible codons. Load it as a single string in
# python and create a list of codons. Make sure they are all uppercase or all
# lowercase.

# codon_string = "AAA AAT AAC aag ATA ATT ATC ATG Aca ACT ACC Acg AGA AGT AGC agG TAA TAT TAC TAG TTA TTT TTC TTG TCA tct TCC tCg TGA TGT TGC TGG CAA CAT CAC CAG CTA cTT ctc CTG CCA CCT CCc CCG CGA CGT CGC cgg GAA GAT GAC GAG GTa GTT GTC GTG GCA GCT GCC GcG"
# codon_upper = codon_string.upper()
# codon_list = codon_upper.split(" ")
# print(codon_list)

# -----------------------------------------------
# 4. From the list created in the previous exercise, remove all codons that
# result in the amino acid Leucine.

# leu_codon = ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"]
# for i in range(len(leu_codon)):
#         codon_list.remove(leu_codon[i])
# print(len(codon_list))


# ----------------------------------------------------
# 5__Create the same list of codons totally in python starting with the string
# ‘ATCG’. *
# Hint: For loops can also be used to iterate through lists, sets, tuples, and
# dictionaries.


seq = "ATCG"


# codon_set= set(())

# for i in range(1,1000):
#     one = random.choice(seq)
#     two = random.choice(seq)
#     three = random.choice(seq)
#     codon= one+ two+ three
#     codon_set.add(codon)

# print(codon_set)
# print(len(codon_set))

# way two
# codon_2 = list(())
# for num1 in seq:
#     for num2 in seq:
#         for num3 in seq:
#            codon_2.append(num1 + num2+ num3)

# print(codon_2)
# print(len(codon_2))
# -----------------------------------------------
# 2.2. Dictionaries
# 1. This week you have bought four apples, two pears and two oranges. You
# want to keep track of them using a dictionary. Try two ways of creating
# this dictionary:
#       (1) Define an empty dictionary syntax and then populate it using the
#           assignment syntax.

# fruit_dic = dict([])
# fruit_dic["apples"] = 4
# fruit_dic["pears"] = 2
# fruit_dic["oranges"] = 2
# print(fruit_dic)

#       (2) Define an already populated dictionary using the curly-braces
#           syntax.Print the final results to verify.

fruit_dic = {'apples': 4, 'pears': 2, 'oranges': 2}
print(fruit_dic)

# a) Now you have bought two more pears, five more oranges and one
#     watermelon. Update the existing values in the dictionary to account for
#     this(note that arithmetic operations work in the same way for
# dictionary values).
fruit_dic['pears'] += 2
fruit_dic['oranges'] += 5
# Dic.update({x : y}), fruit_dict["watermelons"] = 1
fruit_dic.update({"watermelon": 1})
print(fruit_dic)

#     b) Iterate through the keys of the dictionary and for each key print a line
#     showing what fruit it is and how many pieces of that fruit you own.
#         Example output:
# apple: 25 pieces
# orange: 10 pieces
# ... and so on
'''Do the same, but make sure the fruits are printed in alphabetic order.
for i in sorted(fruit_dic):
    print (i, ":", fruit_dic[i])

'''
#


# 2. Your friend didn’t know about your fruit list, and independently made
# their own list. They kindly provided you a Python one-liner to load this
# list into another variable friend_week_fruits. Load this into your terminal
# / script. *
friend_week_fruits = {'apples': 2, 'pears': 1, 'oranges': 2, 'waxberry': 4}
# Now, do a joint dictionary summarizing all the fruits. So - all fruits present
# in either dictionary should be present as keys, and when a fruit is present
# in both, you want the total sum. Note that this is a bit tricky. You need to
# consider that each fruit list has unique fruits not present in the other ones.
# Print similarly to in 1-c) and make sure all counts make sense.
print("\n", "------new section-------", "\n")

'''joint_dictionary = dict({})

for fruit in (friend_week_fruits):
    if fruit in friend_week_fruits:
        if fruit not in fruit_dic:
            print(fruit, "in friend and not mine")
        else:
            print( "common fruits: ",fruit)

'''

# %% b)

# 3. Make a tiny tab-separated file containing two columns found below. *
# ProteinID ProteinSeq
# prot1 AGSATGDASD
# prot4 ASLWASLD
# prot9 PPASDSADSAD
# prot2 XXSWKJXS
# prot8 PSOASSADASD
# a) Load the table from file and insert it into a dictionary. Iterate through
# it in same order of the IDs.
# b) Now, iterate through it again, but only print peptides containing
# Tryptophane (W).
# c) Finally, iterate through it, printing entries NOT containing X.
# Hint: Files can be loaded in python using the open(filename, mode) function. The necessary
# arguments are the path for the file and the mode that the file is opened. The mode can be ‘r’ for read,
# ‘w’ for write, and ‘a’ for append. An opened file must be closed after used, using .close() after the
# variable name of the file. Using with open(filename, mode) python closes the file automatically.

# %% b)

# -------------------------------------------------------------------
# 2.3. Sets
# 1. Check if all sequence ids are unique in regions.fna. *
# 2. The file reads_ids.txt contains sequence ids. Check how many of the ids
# that occur in the fasta file reads.fna. Tip: Test the difference in run time
# using a list and a set for looking up ids. *
# 8
# 3. Find the number of fasta sequence ids that are present in both
# regions_sub1.fna and regions_sub2.fna. Then see how many of these ids
# that are not present in regions_sub3.fna. *


# %% 3
# 3. Program control and logic

# 3.1 Loops and conditions
# Hint: many of these exercises assume that you assign different values to a
# variable. This can be hardcoded within the script:
#     #!/usr/bin/python3
# my_name = "Jakob"

# It can also be made interactive - so that the script asks you for the value when
# running it. (More on this on a coming chapter.)

# #!/usr/bin/python3
# my_name = input("Please enter your name: ")
# Then, when you run it, it will ask you for input.

# $ ./my_script.py
# Please enter your name: < Enter your name here, and press enter >

# %%
# 6. Giving special treatment to yourself. Write a script which first figures out
# if you or someone else is using it, and then greets the user. If it is you, give
# yourself an extra nice greeting.
name = input("who are you and what are you doing?")
if name == "Arash":
    print("hey Arash")


# %% b)
# Use a variable and an if-else statement. Either hard-code the value of the
# variable, or read it using the input function. Check in an if-statement
# whether the variable contains yours or someone else’s name. Prepare two
# different print-statements - one for you and one for everyone else.
# When used, it should give an output similar to the following:
# $ ./greeting.py
# What is your name: Yourname
# So very nice to see you Yourname!
# $ ./greeting.py
# What is your name: Someoneelse
# Hi Someoneelse


# %% b)
# 7. Giving different special treatment to your friends. You want to greet your
# friends too, but realize that you want to keep the very special greeting for
# yourself.
# Rewrite the script from the previous script so that your friends receive a
# greeting different from yours. You still want to get the very special
# greeting yourself, and to give the bland, neutral greeting to people you
# don’t know.
# It should give an output similar to the following:
# $ ./greeting.py
# What is your name: Yourname
# So very nice to see you Yourname!
# $ ./greeting.py
# What is your name: Randomperson
# Hi Randomperson
# $ ./greeting.py
# What is your name: Afriend
# What's up Afriend!


# %% b)
# 8. FizzBuzz simplified. This is inspired by an ( in )famous coding interview
# question claimed to filter out the ‘top percent who actually can program’.
# This is probably an exaggeration, but writing a nice solution can be
# trickier than it first looks!
# Make a script taking a number, and giving one of the following outputs:
# If the number can be divided by three, print "Fizz"
# If the number can be divided by five, print "Buzz"
# If the number can be divided by both three and five, print "FizzBuzz"
# If the number is neither dividable by three nor five, print the number
# The input can either be assigned directly in the script, or read using the
# input function. In the latter case, the input needs to be converted to an
# integer:


for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print(number, "is a FizzBuzz 5 3")
    elif number % 5 == 0:
        print(number, "is a Buzz 5")
    elif number % 3 == 0:
        print(number, "is a Fizz 3")
    else:
        print(number, "not a FizzBuzz")


# 9. Real FizzBuzz. Make your script run over all integers between 1 and 100,
# and print the correct fizz, buzz, fizzbuzz or value for each of them.
# Example output:
# 1
# 2
# fizz
# 4
# buzz
# ...
# 13
# 14
# fizzbuzz
# 16
# ... and so on

# %% b)
# 10. Let’s play golf! You have a golf course with 8 holes. In golf, your score
# depends on the number of strokes required to sink the ball in the hole.
# Your score is compared to the par and has a different name depending on
# the difference. For our course,

# if you used three (or more) strokes less than par, it’s called Albatross,
# two strokes less is Eagle,
# one less is Birdie,
# same as par is Par,
# one more than par is Boogie,
# and two or more is called a Double boogie.
# The par scores for your golf course are coded in a list:# [4,3,5,2,5,4,7,6].

# Make a program that asks the user for the hole they are in
# (1-8) and their number of strokes. Print out the name of the score in that
# hole. For example, 3 strokes on hole 4 is a Boogie (one over par).
hole = int(input("which hole you are? "))
strokes = int(input("how many stroke?"))
list = [4, 3, 5, 2, 5, 4, 7, 6]
par_number = list[(hole-1)]
diff = par_number - strokes
if diff >= 3:
    print("Albatross")
elif diff == 2:
    print("Eagle")
elif diff == 1:
    print("Birdie")
elif diff == 0:
    print("par")
elif diff == -1:
    print("Boogie")
elif diff <= -2:
    print("Double boogie")
else:
    print("what the fuck is this?!")


# %% c)
# 11. Explore how the enumerate() function works:
# Given the following list of letters,
letter_list = ["a", "b", "c", "e", "f", "g", "h", "i"]
print(type(letter_list))
# , write a script that will output the uppercase version of every second
# letter, starting from the first. Use the enumerate() function. The syntax in
# this case is:
enum_list = tuple(enumerate(letter_list[0::2]))
for index, letter in enum_list:
    print(letter.upper())
# for index, letter in enumerate(letter_list):
#     for index

# %%
# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)


# %%
# 12. *You have received the following mRNA sequence, that consists of 10
seq = "UAUAAACGAUACCAUUACUAUGACCAUGGG"
codon_seq = re.findall('...', seq)
print(codon_seq)
for position, codon in enumerate(codon_seq, 1):
    if codon == "UAU" or codon == "UAC":
        print(position, " : ", codon)

textwrapp = wrap(seq, 3)
print(textwrapp)
# You are interested in those codons that encode tyrosine. Knowing that
# they are "UAU" and "UAC", find out in which positions in the sequence
# (what is the number of the codon, out of 10) tyrosine is encoded.
# Hint: you can change the numbering of the indexes output by the
# enumerate() function using the argument start as follows:
# for index, value in enumerate(my_list, start=1):
# ...

# %%
# 13. *Print the first 1000 prime numbers. Hint: to test whether a number is
# prime, it is enough to test whether it is divisible by any prime number
# smaller than half of its value.
prime_numbers = 0
num = 0
while prime_numbers < 100:
    num = num + 1
    count = 1
    for j in range(2, num):
        if num % j == 0:
            count = 0
            break

    if count == 1:
        print(num, end=', ')
        prime_numbers = prime_numbers + 1
        
# WAP to fund first 100 pr
#%%

def getprimes(x):
    primes = []

    for a in range(1,10000):
        isPrime = True
        for b in range(2,a):
            if(a%b==0):
                isPrime = False
        if isPrime:
            primes.append(a)

        if len(primes) == x:
            return primes

print(getprimes(100))

#%%
# Python3 program to display Prime numbers till N
  
#function to check if a given number is prime
def isPrime(n):
  #since 0 and 1 is not prime return false.
  if(n==1 or n==0):
    return False
    
  #Run a loop from 2 to n/2
  for i in range(2,(n//2)+1):
    #if the number is divisible by i, then n is not a prime number.
    if(n%i==0):
      return False
    
  #otherwise, n is prime number.
  return True
  
  
  
# Driver code
N = 100;
#check for every number from 1 to N
for i in range(1,N+1):
  #check if current number is prime
  if(isPrime(i)):
    print(i,end=" ")

# %%


# %%
# 3.2 Error exceptions
# 14. Write a script that asks the user to provide a DNA sequence and raises an
# exception if any non-nucleotide letter is found in the sequence.


# %%
# 15. * Modify the previous script so that the user is prompted to re-enter a DNA
# sequence until all of the nucleotides are valid. Display a message once a
# valid sequence has been entered successfully.
# Example of output:
# Please type a DNA sequence: ACCAB
# Your sequence contains an invalid nucleotide. Please try again.
# Please type a DNA sequence: AGGTAHT
# Your sequence contains an invalid nucleotide. Please try again.
# Please type a DNA sequence: GATC
# You have entered a valid DNA sequence.

# %%
