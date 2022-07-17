import listsplit as l
import Borrow
import Return


def main(): 
    
    while True:  # main loop
    
        print(f'''
||| Welcome to Library Management System|||
-------------------------------------------
-------------------------------------------
      
    1 to display Books
    2 to Borrow a Book 
    3 to Return a Book
    4 to Exit Our Library 
        
-------------------------------------------
       

        ''')

        try:
            # get user input 
            UserInput = int(input("Press Key ------> "))
            if UserInput == 1:
                f = open("Books.txt")
                print(f'''\nAvailable Books in our Library 
-------------------------------''')
                print(f.read() + "\n")
                f.close()
            elif UserInput == 2:
                l.ListSpliting()  
                Borrow.borrow()
            elif UserInput == 3:
                l.ListSpliting() 
                Return.Return()
            elif UserInput == 4:
                print("Thank you for using our Library :)")
                # End Loop
                break  
            else:
                print("Invalid Input, Please choose only from 1-4")
                
                # if invalid input
        except ValueError:  
            print(f"Please Enter a valid number.")


# initialize
main()
