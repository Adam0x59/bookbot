def get_book_text(filepath):
    #Read file into a variable
    with open(filepath) as f:
        file_contents = f.read()
    #print(file_contents)
    
    #Split string into list of words
    file_string_list = file_contents.split()
    #print(file_string_list)
    
    #Get number of words in list
    word_count = len(file_string_list)
    '''
    for word in file_string_list:
        word_count +=1
    '''
    #Print number of words in list to stdout
    print(f"{word_count} words found in the document") 
    
def main():
    get_book_text("books/frankenstein.txt")

main()