#!/usr/bin/env python

import re

# assign the line a vector with zeros if no underline and ones
# if text is underlined
def get_vector_ones(line):
    list_ones =[0]*100
    char_counter = 0
    if '---' in line:
        for char in line: 
            if char == '-':
                list_ones[char_counter] = 1
            char_counter += 1
    return list_ones


# if title in text then add underline it in the output
def add_underline_title(input):
    output = []
    for line in input:
        if line:
            output.append(line.strip())
            if '.-' in line:
                output.append('------------------------------------------')
    return output

def get_underlined_text(text):
   
    text = open('text.txt')

    # for the search windows 4 lines are used simultaneously
    line_0 = ''     # bottom line
    line_1 = ''     
    line_2 = ''     
    line_3 = ''     # upper line

    vect_ones_0 = []   
    vect_ones_1 = []
    vect_ones_2 = []
    vect_ones_3 = []

    s = ''
    counter = 0
    for line in text:
        line_0 = line.rstrip()
        inside_marked_txt = False    # true if char is dashed (in the following line)
        # if title then add marks before and after as the string would be split by '$$'
        if '.-' in line_0:
            line_0 =  '$$ $$' +line_0 +'$$'
        
        # considered underlined when 3 or more dashes are present
        if '---' in line_2:
            vect_ones_2 = get_vector_ones(line_2)
            if '---' in line_0:
                vect_ones_0 = get_vector_ones(line_0)
                
            # iterate for every char in position 'i'
            for i in range(len(line_3)):  
                # construct the string s, adding chars if they are underlined
                if vect_ones_2[i] == 1:    
                    inside_marked_txt = True
                    s += line_3[i]
                #  after an underlined word or parragraph add the mark '$$' 
                if ((inside_marked_txt == True) and (vect_ones_2[i] == 0)):
                    s += ' $$ '
                    inside_marked_txt = False
                # by last char in the row if still underlined then do not add '$$'
                # waiting to continue wuíth the extraction    
                if (vect_ones_2[i] == 1) and (inside_marked_txt == True) and (len(line_3) == i+1): 
                    s += ' '

        vect_ones_3 = vect_ones_2   
        vect_ones_2 = vect_ones_1
        vect_ones_1 = vect_ones_0

        line_3 = line_2
        line_2 = line_1
        line_1 = line_0
        
        counter += 1
    # create a list with the extracted text
    s = s.split('$$')

    return s

text = open('text.txt')

outputlist = get_underlined_text(text)
outputlist = add_underline_title(outputlist)

# write output in txt file
outFile = open('keywords.txt','w')

for line in outputlist:
    outFile.write(line)
    outFile.write('\n')
outFile.close()




