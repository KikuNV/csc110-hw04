# ------------------------------------------------------
#        Name: (put your name here)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ this function will get input from the user and detect if they have used the secret word. Runs an endless loop untill they do. """
    sent =[]
    value = False
    
    sen1 = False
    sen2 = False
    
    
    while sen1 == False and sen2 == False:
        sent = input("Give me a sentence: ").split()
        for elem in sent:
            if elem == secret_word:
                sen1 =True
            elif elem == "dog" or elem == "Dog":
                sen2 = True
                
        if sen1 == False and sen2 == False:
            print("Try again")
        
    if sen1 == True:
        print("You used the secret word!")
    if sen2 == True:
        print("You used the word " "\"dog\"" " or the word" """ "Dog" """)
        
    



# Task 2
def check_greater():
    """ Add your docstring """
    pass



# Task 3
def get_special_numbers():
    """ Add your docstring """
    pass


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

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
