import stats
import sys


def main():
    # If no errors try
    try:
        # If number of arguments provided is not 2, print a message explaining usage
        if len((sys.argv)) != 2:
            print("Usage: python3 main.py <path_to_book>")
            # Exit program after printing usage message
            sys.exit(1)
        # Run word count function & collect outputs
        word_count, file_contents = stats.get_num_words(sys.argv[1])
        # Run character count function & collect output
        char_numbers = stats.get_char_nums(file_contents)
        # Run character count sort function & collect output
        sorted_char_numbers = stats.sorted_list(char_numbers)

        #Get average word length
        average_word_length = stats.get_average_word_length(file_contents)
        
        # Display formatted results
        print("============ BOOKBOT ============")
        print(f"Analysing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("------ Average Word Length ------")
        print(f"Average Word Length: {average_word_length}") 
        print("--------- Character Count -------")
        for char in sorted_char_numbers:
            if (char["char"]).isalpha() == True:
                print(f"{char["char"]}: {char["num"]}")
        print("============= END ===============")
        
    
    # If file not found error occurs print message
    except FileNotFoundError as e:
        print(f"File not found, please check the file exists and try again.\nFile name: \"{sys.argv[1]}\"\n")

main()
