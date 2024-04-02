def ReverseString(Sentence):
    """For an inputted string, reverse and return it"""
    print(Sentence)
    reversed = []
    string_length = int(len(Sentence)) 
    frontways = list(Sentence)
    #print(frontways)

    while string_length != 0:
        new_char = frontways.pop(-1)
        #print(new_char)
        reversed.append(new_char)
        string_length = string_length -1

    print(''.join(reversed))


while True:

    print("\n\tType in a string, and I'll reverse it for you!")
    print("\tType 'q' to quit this application")

    user_input = input("Type in your string here: ")
    if user_input == 'q':
        break
    ReverseString(user_input)
