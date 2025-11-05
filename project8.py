class PassManager():
    def showOptions(self) -> None:
        print('Options:')
        print('1. Add a new account')
        print('2. View saved accounts')
        print('3. Delete all saved data')
        print('4. Quit')

passManager = PassManager()
passManager.showOptions()

while True:
    ask: int = int(input('\nChoose an option: '))
    if ask == 1:
        website: str = input('Website: ')
        username: str = input('Username: ')
        password: str = input('Password: ')
        with open('project8_passwords.txt', 'a') as f:
            f.write(f'Website: {website}\nUsername: {username}\nPassword: {password}\n\n')
        print('Account added!')
    elif ask == 2:
        print('Saved accounts:\n')
        with open('project8_passwords.txt', 'r') as f:
            content = f.read()
            print(content)
    elif ask == 3:
        open('project8_passwords.txt', 'w').close()
        print('All saved data successfully deleted!')
    elif ask == 4:
        print('Goodbye!')
        break