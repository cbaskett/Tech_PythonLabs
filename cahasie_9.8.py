#Cal Hasie
#11/5/12
#Lab 9- 9.8


#This program will capitalize the beginning of the users sentences.
def main():

    #Takes in the users sentences.
    user = input("Please enter the sentences you wish: ")

    #Splits apart each sentence
    sentence_list = user.split('.')

    #Prints the list of sentences
    print(sentence_list)

    #Returns each sentence with the first letter capitalized.
    for sentence in sentence_list:
        sentence = sentence.strip()
        print(sentence.capitalize())

main()

