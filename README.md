## Homework 4

### Task 1: Create a Book class that contains the following:

1.   Constructor with required parameters (ISBN, bookTitle) and optional parameters (averageRating, numbereOfRaters with 0 as default values) initializing the instance variables: (_ISBN,_bookTitle,_averageRating,_numbereOfRaters)
2.   Get methods for _ISBN,_bookTitle, and _numbereOfRaters i.e. getAvgRating, getBookISBN, and getNumberOfRaters.
3.   method addRating that adds one rating by the argument received in the bookRating parameter and increment the number of raters.  This will modify the average rating as follows:<br>
     updatedAverageRating= (currentAverageRating*numberofRaters+newRating)/(numberofRaters+1)<br>
     Also number of raters will increase by 1.<br>
     The average rating will be rounded to 1 digit after decimal point.
4.   method toString that returns a string representing the book data seperated by commas i.e. ISBN, book title, averageRate, numberOfRaters.

### Task 2: write a program that uses the Book class and contains the following:


1. Function: **booksFromFile** that has 1 parameter: bookFile. It reads the book file and returns a list of book objects. The file containing books data is provided. Each line in the file "books.txt" contains ISBN, Book-Title, Average-Rating, and Total-Raters.
2. Function: **rateBooks** that has 1 parameter: bookList. It displays the books in the bookList for rating and request the user to select the book to rate. Then the user will enter the rating from 0 to 5. This function will keep asking the user to rate any book from the list until the user presses ENTER key. Each time it receives a rate, it will update the rating of the corresponding book by calling addRating method of that book.
3.  Function: **writeRatingsToFile** that has 2 parameters: bookList, filename. It takes a list of books and write them to filename using the toString method to create the lines of output in the file. Since the same file used for reading will be used for writing the results.  So the format of the output file is the same as the foramt of the input file.
4. Function: **main** that calls the different functions for reading books data, rating the books, then writing the updated data to the output file. Note that the same file "books.txt" will be used for reading books data at the beginning and writing the updated data at the end. 
