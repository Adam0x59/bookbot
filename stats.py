

def get_num_words(filepath):
    #Read file into a variable
    with open(filepath) as f:
        file_contents = f.read()
    #Split string into list of words
    file_string_list = file_contents.split()
    #Get number of words in list
    word_count = len(file_string_list)
    '''
    for word in file_string_list:
        word_count +=1
    '''
    #Print number of words in list to stdout
    print(f"{word_count} words found in the document") 
