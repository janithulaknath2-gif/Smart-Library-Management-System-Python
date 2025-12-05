Acc_details = {"janithu": "janithu"}
symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "/"]

while True:
    check_have_acc = input(
        "Do You have Acount in Libary management sytem (yes/no) : "
    ).lower()
    if check_have_acc != "yes" and check_have_acc != "no":
        continue
    # --------------Singup_------------------
    if check_have_acc == "no":
        first_name = input("Enter the Your First name : ").lower()
        last_name = input("Enter your last name : ").lower()
        username = first_name + last_name
        print("Your Username is ", first_name + last_name)

        phone_number = input("Enter the Phone number (077 XXX XXXX ): ")
        while len(phone_number) != 10:
            phone_number = input(
                "Please Enter the Valid Phone number (077 XXX XXXX ): "
            )
            if len(phone_number) == 10:
                break

        password = input(
            "Enter the Strong password  (Include : 8 cheracters , symbols (!@#$%^&*) ): "
        ).lower()
        has_sym = False
        for x in symbols:
            if x in password:
                has_sym = True
        while has_sym == False or len(password) < 8:
            password = input(
                "Please Enter the Strong password  (Include : 8 cheracters , symbols (!@#$%^&*) ): "
            )
            has_sym = False
            for x in symbols:
                if x in password:
                    has_sym = True

        Acc_details[username] = password
        check_have_acc = "yes"
        print("sucessfully Created Acount !!!!")

    if check_have_acc == "yes":
        Check_user = input("Enter Your Username: ").lower()
        if Check_user in Acc_details:
            while True:
                Check_password = input("Enter the Password: ")
                if Acc_details[Check_user] == Check_password:
                    print(f" Welcome {Check_user} to Library Management System!")
                    break
                else:
                    print(" Wrong Password! Try again.")
                    continue

        else:
            print(" Username not found! Please create an account.")
            continue
    break


stored_books_details = [
    "Python Basics",
    "Introduction to Programming",
    "Data Structures with Python",
    "Artificial Intelligence Basics",
    "Machine Learning for Beginners",
    "Web Development with HTML",
    "CSS Made Easy",
    "JavaScript Essentials",
    "C Programming Guide",
    "Java for Beginners",
    "Computer Networks",
    "Database Management Systems",
    "Operating Systems",
    "Software Engineering",
    "Cyber Security Basics",
    "Cloud Computing",
    "Data Science Handbook",
    "Algorithms Simplified",
    "Game Development with Python",
    "Flutter App Development",
]

Members_details = {}
fines = []
Return_fines = []
Borrow_books = []


# ----------------------Borrow Book-------------------------------------
def Borrow_book(stored_books_details=stored_books_details):
    c = 0
    while True:
        print("---------Available Books------------")
        for b in stored_books_details:
            c = c + 1
            print(f"{c}. {b}")
        B_book = input("Insert Book Name You want Borrow : ")
        if B_book in stored_books_details:
            stored_books_details.remove(B_book)
            Borrow_books.append(B_book)
            print("Please this book Return to time ")
        else:
            print("This Book is NOT Available in Library")
        checker = input("Do you want Borror a book (yes/no):!!!! ").lower()
        while checker != "yes" and checker != "no":
            checker = input("Do you want Borror a book (yes/no): ").lower()
        if checker == "yes":
            continue
        else:
            break


# --------------------Book Return-------------------------------
def return_book(
    stored_books_details=stored_books_details,
    fines=fines,
    Return_fines=Return_fines,
):
    while True:

        book_name = input("Insert Return Book Name  : ")
        if book_name in stored_books_details:
            print(
                f"This {book_name} book is alredy in Libary, Please Check and Try Again "
            )
            continue
        else:
            stored_books_details.append(book_name)
        if book_name == "" or book_name == " ":
            continue
        Check_late = input(
            f"Do you have late to Return {book_name} (yes/no) : "
        ).lower()
        while Check_late != "yes" and Check_late != "no":
            print("please use yes Or No ")
            Check_late = input(
                f"Do you have late to Return {book_name} (yes/no) : "
            ).lower()
        if Check_late == "yes":
            while True:
                try:
                    days = int(input("How many Days late to Return : "))
                    break
                except ValueError:
                    print("Please Use Numbers !!!")
            fines_cal = 50 * days

        else:
            fines_cal = 0
        Return_fines.append(book_name)
        fines.append(fines_cal)

        c_conti = input("Do you Have Book to Return (yes/no) : ").lower()
        while c_conti != "yes" and c_conti != "no":
            print("please Enter Yes Or NO")
            c_conti = input("Do you Have Book to Return (yes/no) : ").lower()
        if c_conti == "no":
            break
        elif c_conti == "yes":
            continue


# ----------------------Main menu ----------------

while True:
    print("-------------------")
    print("1. Borror Books ")
    print("2. Return Books ")
    print("3. View Stored Books ")
    print(f"4. See all Details of your ")
    print("5. Exit")
    print("-------------------")
    while True:
        try:
            Service_number = int(input("Enter the service Number : "))
            break
        except ValueError:
            print("Please Use Numbers ")
    while 1 > Service_number or Service_number > 5:
        while True:
            try:
                Service_number = int(input("Enter the service Number : "))
                break
            except ValueError:
                print("Please Use Numbers ")
    if Service_number == 1:
        Borrow_book()
    elif Service_number == 2:
        return_book()
    elif Service_number == 3:
        print("---------Available books in Liabary-----------")
        c = 0
        for x in stored_books_details:
            c = c + 1
            print(f"{c}. {x}")
    elif Service_number == 4:
        Members_details[Check_user] = {
            "Total_fines": sum(fines),
            "Return_books": Return_fines,
            "Borrow_books": Borrow_books,
        }
        print("Username : ", Check_user)
        print(f"Total Fines : Rs {sum(fines)}")
        print("-------------------Return Books--------------------")
        for r in Return_fines:
            print(r)
        print("---------------------------------------------------")
        print("------------Borrow Books -------------")
        for b in Borrow_books:
            print(b)
        print("---------------------------------------")
    else:
        break
