
import csv

def readSaveBookInfo() :
    bookList = []

#   Uncomment below code for testing
#     with open("BOOK.csv", "a") as outfile :
#             writer = csv.writer(outfile, lineterminator = "\n")
#             writer.writerows(bookList)
#     return
        
    while True :
        bookNo, title, author, price = input("Enter book num, title, author and price : ").split() 
        price = int(price)
        bookList.append([bookNo,title,author,price])
        ch = input("Enter Y/N to enter more : ")
          
        if(ch.upper() == 'N'):
            with open("BOOK.csv", "a") as outfile :
                writer = csv.writer(outfile, lineterminator = "\n")
                writer.writerows(bookList)
            break
    



def searchBookByAuthor():    
    author = input("Enter author name:")
    with open("BOOK.csv") as outfile:
        reader = csv.reader(outfile)
        result = []
        for row in reader:
            if row[2] == author:
                result.append(row)

        if result == []:
            print("No book found")
            return
        
        print("Books with the specified author are...")
        for line in result:
            print(line)




def searchBookByPrice():
    price = int(input("Enter the price :"))
    with open("BOOK.csv") as outfile:
        reader = csv.reader(outfile)
        result = []
        for row in reader:
            if int(row[3]) <= price:
                result.append(row)

        if result == []:
            print("No book found")
            return
        print("Books with the specified author are...")
        for line in result:
            print(line)
    


def searchBookByTitle():
    author = input("Enter book title:")
    with open("BOOK.csv") as outfile:
        reader = csv.reader(outfile)
        result = []
        for row in reader:
            if row[1] == author:
                result.append(row)

        if result == []:
            print("No book found")
            return
        
        print("Books with the specified title are...")
        for line in result:
            print(line)



def main() :
    menu_dict = {0:readSaveBookInfo, 1:searchBookByAuthor, 2:searchBookByPrice, 3:searchBookByTitle, 4:exit}
    
    while True:
        print("\n(0)Save Book Info (1)Search Book By Author (2)search Book By Price (3)Search Book By Title (4)exit")
        choice = int(input("Enter option >> "))
        func = menu_dict.get(choice)
        if choice == 4:
            break
        if func == None :
            print("Please enter the valid option")
            continue
        func()


if __name__ == '__main__' :
    main()









