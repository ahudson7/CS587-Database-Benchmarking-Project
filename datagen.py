"""
Wisconsin Benchmark Data Generation

This program generates a set of data that is representative of data used in the Wisconsin DB Benchmark.
It operates by generating a DataFrame that contains the data and outputs it as a CSV file.  The number
of tuples and name of the file output can be easily modified under the 'User-Specifications' section.
"""

import pandas as pd

''' User Specifications '''
total_tuples = 10000              # number of tuples generated
output_filename = 'TenKTup.csv'     # name of output file generated

''' Preparing DataFrame and Variables '''
# creating DataFrame
columns = ['unique1', 'unique2', 'two', 'four', 'ten', 'twenty', 'onePercent', 'tenPercent', 'twentyPercent', 'fiftyPercent', 'unique3', 'evenOnePercent', 'oddOnePercent', 'stringu1', 'stringu2', 'string4']
#columns = ['unique1', 'unique2', 'two', 'four', 'ten', 'twenty', 'onePercent', 'tenPercent', 'twentyPercent', 'fiftyPercent', 'evenOnePercent', 'oddOnePercent', 'stringu1', 'stringu2', 'string4', 'stringu1a', 'stringu2a', 'string4a']
data = pd.DataFrame(index = range(0, total_tuples), columns = columns)

# setting up preliminary variables
even = 0
odd = 1
char2_tracker = 0
char3_tracker = 0
x_str_25 = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
x_str_24 = 'xxxxxxxxxxxxxxxxxxxxxxxx'

x_str_45 = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
x_str_48 = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

''' Functions '''

# Function that takes in a numerical value and outputs a corresponding string in the
# form of 7 significant chars followed by 45 'x' chars.  Designed specifically to turn
# the 'unique#' field value into a corresponding string.
def str_generator(unique):
    tmp_str = ''
    final_str = ''
    
    count = 0
    while(unique > 0):
        rem = unique % 26
        tmp_str += chr(65 + rem)
        count += 1
        unique = unique//26

    for i in range (0, 7-count):
        final_str += 'A'
    
    final_str += tmp_str
    final_str += x_str_45
    
    return(final_str)

# generating data within the DataFrame that needs to be in randomized order
for i in range(0, total_tuples):
    
    '''
    # handles generation of old string format used in prior versions of Wi. Benchmark
    # handling stringu1
    char1 = 65 + i%22
    if i%22 == 0 and i != 0:
        char2_tracker += 1
        char2_tracker = char2_tracker%22
    
    if i%(pow(22, 2)) == 0 and i != 0:
        char3_tracker += 1
        char3_tracker = char3_tracker%22
    
    char2 = 65 + char2_tracker
    char3 = 65 + char3_tracker
    '''
    
    data.loc[i, 'unique1'] = i
    data.loc[i, 'two'] = i%2
    data.loc[i, 'four'] = i%4
    data.loc[i, 'ten'] = i%10
    data.loc[i, 'twenty'] = i%20
    data.loc[i, 'onePercent'] = i%100
    data.loc[i, 'tenPercent'] = i%10
    data.loc[i, 'twentyPercent'] = i%5
    data.loc[i, 'fiftyPercent'] = i%2
    data.loc[i, 'unique3'] = i
    data.loc[i, 'evenOnePercent'] = even%200
    data.loc[i, 'oddOnePercent'] = odd%200
    data.loc[i, 'stringu1'] = str_generator(i)
    #data.loc[i, 'stringu1a'] = chr(char1) + x_str_25 + chr(char2) + x_str_24 + chr(char3)  // old string format
    even += 2
    odd += 2

# shuffling contents of DataFrame
data_final = data.sample(frac = 1)
data_final = data_final.reset_index(drop=True)

'''
# used in generation of old string format
# resetting trackers
char2_tracker = 0
char3_tracker = 0
'''

# generating data within the DataFrame that is in a specific order
for i in range(0, total_tuples):
    
    '''
    # handles generation of old string format used in prior versions of Wi. Benchmark
    # handling stringu2
    char1 = 65 + i%22
    
    if i%22 == 0 and i != 0:
        char2_tracker += 1
        char2_tracker = char2_tracker%22
    
    if i%(pow(22, 2)) == 0 and i != 0:
        char3_tracker += 1
        char3_tracker = char3_tracker%22

    char2 = 65 + char2_tracker
    char3 = 65 + char3_tracker
    '''
    
    # handling string4
    str4_mod = 65 + (7*(i%4))
    
    data_final.loc[i, 'unique2'] = i
    data_final.loc[i, 'stringu2'] = str_generator(i)
    data_final.loc[i, 'string4'] = chr(str4_mod) + chr(str4_mod) + chr(str4_mod) + chr(str4_mod) + x_str_48
    #data_final.loc[i, 'stringu2a'] = chr(char1) + x_str_25 + chr(char2) + x_str_24 + chr(char3)            // old string format
    #data_final.loc[i, 'string4a'] = chr(str4_mod) + x_str_25 + chr(str4_mod) + x_str_24 + chr(str4_mod)    // old string format
    
# saving output file
#data_final.to_csv(output_filename, index=False)
