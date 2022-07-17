import datetime 

dt1 = datetime.datetime.now()


#  date function
def getCurrentDate() :
    
    """gets current date in string"""
    return str(dt1.date())

# time func
def getCurrentTime() -> str:
    
    """gets current time in string"""
    return str(dt1.time())

#get date from current date 
def getDate() -> datetime:
    
    #return deadline
    date = getCurrentDate().split('-')
    return datetime.date(int(date[0]), int(date[1]), int(date[2]))

# get borrowed date 
def getBorrowedDate(file) -> datetime:
    f = open(file) 
    lines = f.readlines()
    f.close()
    for data_line in lines:
        if 'Date:' in data_line:
          #(seperate date , lines and - )
            data = data_line.strip().strip('Date:').strip('\n').split('-')
            return datetime.date(int(data[0]), int(data[1]), int(data[2]))
