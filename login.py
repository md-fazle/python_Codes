def login():
    userName=input("Enter your User Name:")
    userPasswrod=input("Enter your Password:")

    valid_user=["user1","user2","Fazle"]
    valid_pass=["this1","is2","it100"]

    if userName is valid_user and userPasswrod == valid_pass[valid_user.index(userName)]:
        print("login successfull!")
    else:
        print("invalid username or password")
login()