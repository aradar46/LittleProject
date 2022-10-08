#!/usr/bin/python3

# my libraries

# variables definitions


# reading fasta sequences
malaria_fna = open("malaria.fna", "r")
malaria_fna_data = malaria_fna.read()
# print(malaria_fna_data)
malaria_fna.close()


# reading blastx file
malaria_blastx = open("malaria.blastx.tab", "r")
malaria_blastx_data = malaria_blastx.read()
# print(malaria_blastx_data)
malaria_blastx.close()

# merging file


'''
with open("Test_read.txt", 'r') as txt:
    for line in txt:
        print(line.strip('\n'))

#%%
f = open("malaria.fna", "r")
line = f.readline()
while line:
    line = f.readline()
    print(line)
f.close()
'''

# %%
