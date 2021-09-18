books = ['A234', 'A675', 'A212', 'B671', 'B534', 'B777', 'B778', 'B812', 'C101', 'C102']
borrowers = ['L34', 'L22', 'L19', 'L84', 'L77']
#The book that has been checked out will be stored in this dictionary together with borrower id.
#The book that has been returned will be deleted in this dictionary together with borrower id.
book_borrowed_dict = {'C102': 'L77'}

def process_input(action_input:str, borrower_id:str, book_id:str):

    if action_input == 'checkout' or action_input == 'return':  #need to seperate the strings to give if judgment
        if book_id not in books:
            print('there is no such book', book_id)
            print(books)
        elif borrower_id not in borrowers:
            print(borrower_id, 'is not a valid borrower')

        if action_input == 'checkout':
            if book_id in book_borrowed_dict:
                print(book_id + "already checked out")

            else:
                book_borrowed_dict[book_id] = borrower_id  #book_id is the key, borrower_id is the value, put that borrowed book in the dictionary
                print("checkout successful")


        elif action_input == 'return':
            if book_id in book_borrowed_dict:
                if book_borrowed_dict[book_id] == borrower_id: #confirmed that key(book id) and value(borrower_id) is matched
                    del book_borrowed_dict[book_id]
                    print("return successful")
            else:
                print(book_id + " not currently checked out")

    elif action_input == 'exit':
        exit()
    else:
        print("Not a valid command. Please try again")





