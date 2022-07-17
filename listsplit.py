#dictionary for seperating values 
List= {
    'name': [],    'author': [],    'quantity': [],    'price': [] }


def ListSpliting():
   #reading the txt file 
    f = open("Books.txt")
    detail = [s.strip("\n") for s in f.readlines()]  # read and strip down line breaks, store lines in an array
    f.close()
    for i in range(len(detail)):
        
        j = 0  # 
        # Spliting , from the list 
        
        for s in detail[i].split(","):
            
         
            if j == 0:  
                List['name'].append(s) 
                
            elif j == 1:
                List['author'].append(s)
                
            
            elif j == 2:
                # append into quantity in int datatype
                List['quantity'].append(int(s))
                
            
            elif j == 3:

                 # remove $ and append in float datatype
                List['price'].append(float(s.strip("$"))) 
            j += 1
            
