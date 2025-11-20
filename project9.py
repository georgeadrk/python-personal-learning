class PassManager():
    def showOptions(self) -> None:
        print("Options")
        print("1. Add a new account")
        print("2. View saved accounts")
        print("3. Delete all saved data")
        print("Quit")

    def addAccount(self) -> None:
        web = input("Website: ")
        usn = input("Username: ")
        pw = input("Password: ")

