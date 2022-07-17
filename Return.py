import DateTime as dt
import listsplit as l


def Return():
   
    
    num1 = 1
    
    
    name = input("Enter your first name: ")
    
    outputborrow =f"Book Transaction\Borrowed By {name}.txt"
    outputreturn = f"Book Transaction\Returned by {name}.txt"
    
    
    try:
        #Book transaction note
        f = open(outputborrow)  # opens in read mode by default
        data = f.read()
        print(data)
        f.close()
        f = open(outputreturn, "w+")
        f.write(f'''Library Management System:Book Transaction (Return)
 --------------------------------------------------\n
    Borrowed by: {name} 
    Date: {dt.getCurrentDate()}
    Time: {dt.getCurrentTime()}
    S.N.\tBook Name\t\t\t\t\tAuthor\t\t\t\tCost\t\t\tQuantity\n''')
        f.close()

        totalcost = 0.0
        for i in range(7):
            book = l.List['name'][i]
            if book in data:
                f = open(outputborrow)  
                
              
                allbooks = f.read().count(book)
                l.List['quantity'][i] += allbooks
                f.close()
               # append to new transaction to txt file 
                f = open(outputreturn, "a")  
                f.write(f"\t{num1} \t{book}\t\t\t\t\t{l.List['author'][i]}\t\t\t{l.List['price'][i]}"
                     
                        f"\t\t\t\t{allbooks}\n")
                num1 += 1
                f.close()
                totalcost += l.List['price'][i] * allbooks
                # total cost 
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t${totalcost}")
        # Checling for fine 
        days = (dt.getDate() - dt.getBorrowedDate(outputborrow)).days
        print(f"Returned After {days} days")
        if days > 10:
            fineapplied = 2 * (days - 10)
            f = open(outputreturn, "a")
            f.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFine: ${fineapplied}\n")
            f.close()
            totalcost += fineapplied

        print(f"Total Price: ${totalcost}")

        f = open(outputreturn, "a")
        f.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTotal: ${totalcost}")
        f.close()
# open stock and update bookstock
        f = open("Books.txt", "w+")
        for i in range(7):
            # updating book stock
            f.write(f"{l.List['name'][i]},{l.List['author'][i]},"
                    f"{l.List['quantity'][i]},${l.List['price'][i]}\n")
        f.close()
         #if User name doesnot match  exception errors
    except FileNotFoundError:   
    
    
   
        print("\nUser Not found in our catalogue!!\n ")
        Return()
