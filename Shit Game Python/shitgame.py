# Word Shit
def main():

    print("Welcome to Shit Game! In this game you have to guess only 1 word. Good Luck as the word it's really hard and you probably gonna cry and rage quit like a dummy :3\n")
    print("Made By : ImBilly\n")
    print("Enjoy this shit game\n")

    print("Guess the word! Starts with 'S' Ends with 'T' S _ _ T\n")

    first_letter = input("First letter: ")

    if first_letter == "S":
        print("Yup!")

    elif first_letter == "s":
        print("Yup!")

    else:
        print("Wrong letter :/\n")
        


    second_letter = input("Second letter: ")

    if second_letter == "H":
        print("Yup!")

    elif second_letter == "h":
        print("Yup!")

    else:
        print("Wrong letter :/\n")


    third_letter = input("Third letter: ")

    if third_letter == "I":
        print("Yup!")
        
    elif third_letter == "i":
        print("Yup!")

    else:
        print("Wrong letter :/\n")


    fourth_letter = input("Fourth letter: ")

    if fourth_letter == "T":
        print("Yup!")

    elif fourth_letter == "t":
        print("Yup!")

    else:
        print("Wrong letter :/\n")


    word = first_letter + second_letter + third_letter + fourth_letter

    print(word)
    print(" ")

    if word == "SHIT":
        print("Correct!")

    if word == "shit":
        print("Correct!")


    restart = input("Would you like to restart? (yes/no) ")
    if restart == "yes":
        main()
    elif restart == "no\n":
        closeInput = input("Press ENTER to exit")
        print("Closing...")
main()