restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'x',      'o',      'o',      'o',      'x'],
    [2,        'x',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'x',      'x',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'x',      'x',      'o',      'o',      'x',      'o']
]

# Using restaurant tables 2 for all the testing.

#LEVEL 1
# Listing all the tables that are free or 'o'
# Use a loop to iterate through all the tables, find a way to skip the first row
# Whatever table is free, you print it. 

# work through columns by calling each list in every index
# Make a list to keep track of all tables that are free
def free_tables(tables):

    # https://www.w3schools.com/python/python_strings_slicing.asp 
    # Used this code to figure out how to start from the 2nd row instead of the first row the [:1]
    
    # Table are the ROWS 
    # I had to do multiple for loops because I couldn't figure out how to get nested loops to work...
    # Instead I just checked ever column using indexes seperately
    for table in tables[1:]:
            if table[1] == "o":
                print("table 1 is free")
                break

    for table in tables[1:]:
        if table[2] == "o":
            print("Table 2 is free")
            break

    for table in tables[1:]:
        if table[3] == "o":
            print("Table 3 is free")
            break

    for table in tables[1:]:
        if table[4] == "o":
            print("Table 4 is free")
            break
    
    for table in tables[1:]:
        if table[5] == "o":
            print("Table 5 is free")
            break
    
    for table in tables[1:]:
        if table[6] == "o":
            print("Table 6 is free")
            break

free_tables(restaurant_tables2)
#This was the lvl 1 test

#LEVEL 2



#Write code that checks the party size
# Has to make sure that the table is free and has the party size available