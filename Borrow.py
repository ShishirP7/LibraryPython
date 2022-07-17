import DateTime as dt
import listsplit as l


def borrow():
    #input from users
    
    while True:  
        
        firstname = input("Enter your first name: ")           
        if firstname.isalpha():            
            break         
        print("\nPlease Enter Your Name Correctly!!")  
        
    while True:   
        
        lastname = input("Enter your last name: ")        
        if lastname.isalpha():            
            break        
        print("\nPlease Enter Your Name Correctly!!")
      #creating an transaction txt file   
    output = f"Book Transaction\Borrowed By {firstname}.txt"
    # open and writing in txt file 
    f = open(output, "w+")
    
   
    f.write(f''' Library Management System: Book Transaction (Borrow) 
 ---------------------------------------------------\n
    Borrowed by: {firstname} {lastname} 
    Date: {dt.getCurrentDate()}
    Time: {dt.getCurrentTime()}\n
    S.N.\tBook Name\t\t\t\t\t\tAuthorname\t\t\t\t\t\tCost\n''')
    f.close()

    num = 1
    
    # for listing books 
    while True: 
       
        print(f'''\nBooks In our Library : 
----------------------''')
        [print(f"Enter {i} to borrow  {l.List['name'][i]}\t ")for i in range(len(l.List['name']))]

        try:
            index = int(input("\nWhich Book You would Like to Borrow??"))
            try:  
                if l.List['quantity'][index] > 0:
                    print("\n You Have Successfully Borrowed a Book .")
                    
                   
                    
                    #  append trasaction to txt file 
                    f = open(output, "a")  
                    f.write(
                        f"\t{num} \t{l.List['name'][index]}\t\t\t\t\t{l.List['author'][index]}"
                        f"\t\t\t\t\t\t{l.List['price'][index]}\n")
                    f.close()
                    #for Output in console
                    f = open(output) 
                    data = f.read()
                    print(data)
                    f.close()
                    print(" Please Return it within 10 Days !")
                    
                    #for updating book stocks in the library 
                    l.List['quantity'][index] -=  1
                    f = open("Books.txt", "w+")
                    for i in range(7):
                        f.write(
                            f"{l.List['name'][i]},{l.List['author'][i]},"
                            f"{l.List['quantity'][i]},${l.List['price'][i]}\n")
                    f.close()
                    option = input(f'''Press (Y) If you want to borrow more Books: 
Press Enter If you want to exit--> ''')
                    if option.lower() != "y":
                        break  # end loop
                    num += 1
                else:
                    print("Sorry !!! Book is Unavailable at the moment ")
                    #exception errors
            except IndexError:
                print("\nPlease Enter the Valid Book Number.\n")
        except ValueError:
            print(f"\n Input not valid .\n")
