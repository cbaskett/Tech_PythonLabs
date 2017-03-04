#Cal Hasie
#11/5/12
#Lab 9- 9.4



#Runs a Programs that translates morse code into text.
def main():

    #Copy of morse code from the file provided
    morse_code = [' ', '-....', '--.', '--.-', '--..--', '--...', '....', '.-.', '.-.-.-', '---..', '..', '...', '..--..', '----.', '.---', '-', '-----', 
                     '.-', '-.-', '..-', '.----', '-...', '.-..', '...-', '..---', '-.-.', '--', '.--', '...--', '-..', '-.', '-..-', '....-', '.', '---', '-.-', '.....', '..-.', '.--.', '--..']
    
    #Gets users input on what to change into morse code
    user = input('Please enter a name or a sentence ')
    print('The morse code for', user, 'is ')

    #Runs a loop that searches for each individual character and determines
    #the morse code with regard to the index number
    for ch in user:
        if ch == ' ':
            print(ch, ' ', morse_code[0])
        elif ch == '6':
            print(ch, ' ', morse_code[1])
        elif ch == 'G' or ch == 'g':
            print(ch, ' ', morse_code[2])
        elif ch == 'Q' or ch == 'q':
            print(ch, ' ', morse_code[3])
        elif ch == ',':
            print(ch, ' ', morse_code[4])
        elif ch == '7':
            print(ch, ' ', morse_code[5])
        elif ch == 'H' or ch == 'h':
            print(ch, ' ', morse_code[6])
        elif ch=='R' or ch == 'r':
            print(ch, ' ', morse_code[7])
        elif ch == '.':
            print(ch, ' ', morse_code[8])
        elif ch == '8':
            print(ch, ' ', morse_code[9])
        elif ch == 'I' or ch == 'i':
            print(ch, ' ', morse_code[10])
        elif ch == 'S' or ch == 's':
            print(ch, ' ', morse_code[11])
        elif ch == '?':
            print(ch, ' ', morse_code[12])
        elif ch == '9':
            print(ch, ' ', morse_code[13])
        elif ch == 'J' or ch == 'j':
            print(ch, ' ', morse_code[14])
        elif ch == 'T' or ch == 't':
            print(ch, ' ', morse_code[15])
        elif ch == '0':
            print(ch, ' ', morse_code[16])
        elif ch == 'A' or ch == 'a':
            print(ch, ' ', morse_code[17])
        elif ch == 'K' or ch == 'k':
            print(ch, ' ', morse_code[18])
        elif ch == 'U' or ch == 'u':
            print(ch, ' ', morse_code[19])
        elif ch == '1':
            print(ch, ' ', morse_code[20])
        elif ch == 'B' or ch == 'b':
            print(ch, ' ', morse_code[21])
        elif ch == 'L' or ch == 'l':
            print(ch, ' ', morse_code[22])
        elif ch == 'V' or ch == 'v':
            print(ch, ' ', morse_code[23])
        elif ch == '2':
            print(ch, ' ', morse_code[24])
        elif ch == 'C' or ch == 'c':
            print(ch, ' ', morse_code[25])
        elif ch == 'M' or ch == 'm':
            print(ch, ' ', morse_code[26])
        elif ch == 'W' or ch == 'w':
            print(ch, ' ', morse_code[27])
        elif ch == '3':
            print(ch, ' ', morse_code[28])
        elif ch == 'D' or ch == 'd':
            print(ch, ' ', morse_code[29])
        elif ch == 'N' or ch == 'n':
            print(ch, ' ', morse_code[30])
        elif ch == 'X' or ch == 'x':
            print(ch, ' ', morse_code[31])
        elif ch == '4' or ch == '4':
            print(ch, ' ', morse_code[32])
        elif ch == 'E' or ch == 'e':
            print(ch, ' ', morse_code[33])
        elif ch == 'O' or ch == 'o':
            print(ch, ' ', morse_code[34])
        elif ch == 'Y' or ch == 'y':
            print(ch, ' ', morse_code[35])
        elif ch == '5':
            print(ch, ' ', morse_code[36])
        elif ch == 'F' or ch == 'f':
            print(ch, ' ', morse_code[37])
        elif ch == 'P' or ch == 'p':
            print(ch, ' ', morse_code[38])
        elif ch == 'Z' or user == 'z':
            print(ch, ' ', morser_code[39])
        else:
            print("Invalid input")
        



main()
