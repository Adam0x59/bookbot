import statistics
import string
import re

def get_num_words(filepath):
    #create file contents variable
    with open(filepath) as f:
        file_contents = f.read()
    #Split string into list of words
    file_string_list = file_contents.split()
    #Get number of words in list
    word_count = len(file_string_list)
    #Return word_count and file_contents
    return word_count, file_contents

def get_char_nums(file_contents):
    #Create dictionary to store counts
    char_numbers = {}
    #Iterate through charecters in file_contents string
    for char in file_contents:
        #Convert character to lowercase if required
        char = char.lower()
        #Check dictionary to see if character key exists
        if char in char_numbers:
            #Increment key's value if it exists
            char_numbers[char] += 1
        #If character does not exist as a key create the key    
        else:
            #Create missing key, set value to 1
            char_numbers[char] = 1
    #Return the dictionary of character keys and their counts        
    return char_numbers


def sorted_list(char_numbers):
    #Create empty list to store dictionaries
    sorted_char_numbers = []
    #Iterate through dictionary of char_numbers
    for char in char_numbers:
        #Populate list with dictonaries
        sorted_char_numbers.append({"char":char, "num":char_numbers[char]})
    #A function to return dictionary value from given key for .sort(function)
    #.sort requires keyword arguments...
    def sort_on(dict):
        return dict["num"]
    #Sort list of dictionaries in descending order based on "num" key
    sorted_char_numbers.sort(reverse=True, key=sort_on)
    #return the sorted list
    return sorted_char_numbers

def get_average_word_length(file_contents):
    #Remove punctuation from the string
    translator = str.maketrans('', '', string.punctuation)
    clean_text = file_contents.translate(translator)
    #Create a list of words
    word_list = clean_text.split()
    #count words in the list
    word_char_count_list = [len(word) for word in word_list]
    return statistics.mean(word_char_count_list) if word_char_count_list else 0

def get_average_sentence_length(file_contents):
    # Split on period, exclamation mark, or question mark followed by space or end of text
    sentences = re.split(r'[.!?](?:\s|$)', file_contents)
    # Remove empty or whitespace-only strings
    sentences = [s.strip() for s in sentences if s.strip()]
    # Avoid division by zero
    if not sentences:
        return 0 
    # Count and accumulator init
    sentence_count = 0
    sentence_lenght_accumulator = 0
    # Calculate averages and return.
    for sentence in sentences:
        sentence_count += 1
        sentence_lenght_accumulator += len(sentence.split())
    return sentence_lenght_accumulator / sentence_count

