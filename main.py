def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_text = file_contents.lower()
        print("--- Begin report of books/frankenstein.txt")
        print (f"{len(file_contents.split())} words found in the document\n")
        char_counts = count_characters(lowered_text)
        print(sort_on(char_counts))
        print("--- End report ---")

def count_characters(lowered_text):
    char_counts = {}
    for char in lowered_text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(dict):
    char_list = []
    returned_string = ""
    for key in dict:
        if key.isalpha():
            a = {'Letter': key, 'Count': dict[key]}
            char_list.append(a)
    char_list.sort(reverse=True, key=lambda item: item['Count'])
    for index in range(len(char_list)):
        #print(f"TEST {char_list[index]['Letter']} + {char_list[index]['Count']}")
        returned_string += f"The '{char_list[index]['Letter']}' character was found {char_list[index]['Count']}\n"
    return returned_string

main()