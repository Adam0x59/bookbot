def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    #print(file_contents)
    file_string_list = file_contents.split()
    #print(file_string_list)
    word_count = 0
    for word in file_string_list:
        word_count +=1
    print(f"{word_count} words found in the document") 

def main():
    get_book_text("books/frankenstein.txt")

main()