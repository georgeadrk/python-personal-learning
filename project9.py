class PassManager():
    def showOptions(self) -> None:
        print("Options")
        print("1. Add a new account")
        print("2. View saved accounts")
        print("3. Delete all saved data")
        print("4. Quit")

    def addAccount(self) -> None:
        web: str = input("Website: ")
        usn: str = input("Username: ")
        pw: str = input("Password: ")

        with open('project9_passwords.txt', 'a') as f:
            f.write(f'Website: {web}\nUsername: {usn}\nPassword: {pw}\n\n')
        print('Account added!')

    def viewAccounts(self) -> None:
        print('Saved accounts:\n')
        with open('project9_passwords.txt', 'r') as f:
            content = f.read()
            print(content)

    def deleteAll(self) -> None:
        open('project9_passwords.txt', 'w').close()
        print('All saved data successfully deleted!')

passManager = PassManager()

passManager.showOptions()
while True:
    ans: int = int(input("\nChoose an option: "))

    if ans == 1:
        passManager.addAccount()
    elif ans == 2:
        passManager.viewAccounts()
    elif ans == 3:
        passManager.deleteAll()
    elif ans == 4:
        print("Goodbye!")
        break
    else:
        print("Please retry!")
        continue