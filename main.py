def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

from brian import process_input
if __name__ == '__main__':
    # let users input browser_id, book_id, action type
        print("=========Welcome to the Library Management System==========")
        borrower_id = input("please type one borrower id")
        book_id = input("please type one book id")
        main_prompt = "What is your request? please type 'checkout' if you would like to check out a book. Type 'return' if you would like to return a book. Type 'exit' to terminate LMS.\n" \
                    ">>"
        action_input = input(main_prompt)
        while action_input != "exit":
            process_input(action_input, borrower_id, book_id)
            action_input = input(main_prompt)