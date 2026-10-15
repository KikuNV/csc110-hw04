# ------------------------------------------------------
#        Name: (Kiku Nagai)
#       Peers: (ab mosca)
#  References: (streetgeeks.com (see note))
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ this function will get input from the user and detect if they have used the secret word. Runs an endless loop untill they do. """

    #sen1 checks if the user input a relavant response (dog/s or food)
    sen1 = False

    while sen1 == False:
        UserInput = input("Give me a sentence: ")
        #.lower is a function i found from "streetgeeks.com" to make an input all lowercase. thus allowing for inputs like "Dogs"
        if secret_word in UserInput.lower():
            print("You used the secret word!")
            sen1 = True
        elif "dog" in UserInput.lower():
            print("You used the word \"dog\" or the word \"Dog\"!")
            sen1 = True
        else:
            print("Try again")
            sen1 = False
        

# Task 2
def check_greater():
    """ will take user input and see what value is greater """
    num1 = 0
    num2 = 1
    value = False
    while value == False:
        num1 = int(input("Give me a first integer: "))
        num2 = int(input("Give me a second integer: "))
        if num1 > num2:
            print("First is Greater")
            value = True
        elif num2 > num1:
            print("Second is Greater")
            value = True
        else:
            print("Try again")
            
    
           
        
        
        



# Task 3
def get_special_numbers():
    """ tis function will return the numbers that follow our qualifications"""
    for i in range(1,40):
        if i%2 != 0:
            if i%3 == 0:
                if i%5 != 0:
                    print(i)
                


# Task 4.a
def my_for_loop():
    """ input a string and return whether each letter is a constant or a vowel. """
    i=0
    j=0
    string = (input("Give me a string: "))
    letters = list(string)
#cond25 checks if string input is has 2-5 characters
    cond25 = (2 <= len(string) <= 5)

    if cond25 == False:
        #note for graders: this direction was not specified on git and only in the pytest. You have bad instructions. reccomend updating them to include this.
        print("bad word")
        return
    
    for i in range(i, len(string)):
        #condvowel checks if the letter is a vowel
        condvowel = (letters[i] == "a" or letters[i] == "e" or letters[i] == "i" or letters[i] == "o" or letters[i] == "u" )
        if condvowel == True:
            print(letters[i], "is a vowel")
        else:
            print(letters[i],  "is a consonant")
    
    
        
   
        

# Task 4.b
def my_while_loop():
    """ This while loop allows the user to pick a, repeat menu, b to print goodbye or c to break the loop. """
    realOptionCheck = False
    while realOptionCheck == False:
        option = input("Choose one option: a, b, or c: " )
        #realOptionCheck checks if the user has entered either a, b or c.
        realOptionCheck = (option =="a" or option =="b" or option == "c")
        if realOptionCheck == False:
            print("try again")
        elif option == "a":
            realOptionCheck = False
        elif option == "b":
            print("Goodbye")
            return
        elif option == "c":
            exit()
            print("a")
        
        

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
