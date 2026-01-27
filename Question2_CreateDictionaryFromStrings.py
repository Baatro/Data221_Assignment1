def create_dictionary_from_strings(given_string_list):
    dictionary_of_strings = {}
    # Each key should be a string while values are another dictionary with length of string and if legth is even or odd
    for string in given_string_list:
        string_length = len(string)
        if string_length % 2 == 0: # verify if length is even or odd and store result
            length_is_even = "Even"
        else:                           
            length_is_even = "Odd"
        dictionary_of_strings[string] = {
            "length": string_length,
            "parity": length_is_even
            
        }
    return dictionary_of_strings

# testing using the expected output
test_strings = ["data","science"]
print(create_dictionary_from_strings(test_strings))