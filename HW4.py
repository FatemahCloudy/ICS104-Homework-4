## Creating a file
# just let me generate the file for you ~
# I did that because I can't submit two files for the homework

data = [
            #'ISBN,Book-Title,Total-Rating,Total-Raters',
            '0195153448,Classical Mythology,0,0',
            '0002005018,Clara Callan,0,0',
            '0060973129,Decision in Normandy,0,0',
            '0887841740,The Middle Stories,0,0',
            '0446310786,To Kill a Mockingbird,0,0'
            ]

with open('bookfile.txt', 'w') as file:
    for i in data:
        file.write(i + '\n')

## Task 1

# Create a class that takes the ISBN and title for a book
# it also can take the number and avreage of rating (optional)

class Book:

    def __init__(self, isbn, bookTitle, averageRating = 0 , numberOfRaters = 0):
        self.isbn = isbn
        self.bookTitle = bookTitle
        self.averageRating = averageRating
        self.numberOfRaters  = numberOfRaters

# Those methodes are used to get the data assigned to the object
    def getIsbn(self):
        return self.isbn
    
    def getTitle(self):
        return self.bookTitle
    
    def getAvgRating(self):
        return self.averageRating
    
    def getNumRaters(self):
        return self.numberOfRaters
    
    # this method add a new rate updating the avergae and number of rates
    def addRating(self, rate):
        numberOfRaters = self.numberOfRaters
        averageRating = self.averageRating

        # the mathmaticial equation is used to update the average
        updatedAvg = (averageRating * numberOfRaters + rate) / (numberOfRaters + 1)

        # round to one digit after dicimal
        updatedAvg  = round(updatedAvg, 1)

        # increase the number of raters by 1
        self.numberOfRaters += 1

        # update the value of average
        self.averageRating = updatedAvg
    
    # this method convert the data to a string spliting them by qummas
    def toString(self):
        bookData = (f'{self.isbn}, {self.bookTitle}, {self.averageRating}, {self.numberOfRaters}')
        return bookData

## Task 2
# this function recives a file with books data and convert the data into a list
def BooksFromFile(BookFile):

    with open(BookFile) as books:
        books = [line.strip() for line in books.readline()]

    return books

# this function takes a list of books and display it for rating
def ratBooks(bookList):

    print('The books available for rating are:')
    i = 1

    for book in bookList:
        isbn, bookTitle, avg, number = book.split(',')
        print(f'book id: {i} {bookTitle} Average rating: {float(avg)} from: {number} user(s).')
        i += 1
        

# This function reads books from a file and return a list of book objects
def booksFromFile(bookFile):
    bookList = []

    # Get data from file
    with open(bookFile) as file:

        for line in file:
            isbn, title, rating, raters = line.strip().split(",")
            rating = float(rating)
            raters = int(raters)

            # Add books to the list
            book = Book(isbn, title, rating, raters)
            bookList.append(book)

    return bookList

# This function displays the books and update the ratings
def rateBooks(bookList):

    while True:

        # Print a message to the user
        print("Please select a book to rate from the following list:")

        # Loop through the book list and print the informations
        with open('BookFile.txt') as books:
            books = [line.strip() for line in books.readlines()]
            i = 1

            for book in books:
                isbn, bookTitle, avg, number = book.split(',')
                print(f'book id: {i} {bookTitle} Average rating: {float(avg)} from: {number} user(s).')
                i += 1

        # Get the user input for the book index
        bookId = input("Enter the book index or press ENTER to quit: ")

        # End when the user press Enter
        if not bookId:
            break

        # if not empty, convert to integer and check if valid
        bookId = int(bookId)

        if 1 <= bookId <= len(bookList):
            book = bookList[bookId - 1] # the list's index starts from 0

            while True:
                rating = input("Enter your rating from 0 to 5: ")

                if not rating.isdigit():
                    print('rating must be an integer between 0 and 5')

                else:
                    rating = int(rating)

                # If the rating is valid add the rating to the book object
                    if 0 <= rating <= 5:
                        book.addRating(rating)
                        break

                    else:
                        # Print an error message
                        print('rating must be between 0 and 5')
        else:
            # Print an error message
            print('You did not enter correct book id')

# This function to write the books to a file using the toString method
def writeRatingsToFile(bookList, filename):

    # Write the book object as a string to a file
    with open(filename, 'w') as file:

        for book in bookList:
            file.write(book.toString() + '\n')

# This function call the other functions to make up the system
def main():

    # Read the books from the file
    bookList = booksFromFile('bookfile.txt')

    # Display the books for rating and update the ratings
    rateBooks(bookList)

    # Write the updated books to the file
    writeRatingsToFile(bookList, 'bookfile.txt')

    # Print a thank you message
    print('Thanks for using the book rating app')

# Call the main function
main()
