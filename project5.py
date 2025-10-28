tasks: list[str] = []

print('==== TO-DO LIST ====')
print('1. View tasks')
print('2. Add tasks')
print('3. Remove tasks')
print('4. Quit')

while True:
    option: int = int(input('\nChoose an option: '))

    if option == 1:
        if len(tasks) == 0:
            print('The task list is empty!')
            continue
        else:
            num: int = 1
            for task in tasks:
                print(f'{num}. {task}')
                num += 1
        continue
    elif option == 2:
        new_task: str = input('Enter a new task: ')
        tasks.append(new_task)
        print('Task added!')
        continue
    elif option == 3:
        rem_task: str = input('Remove the first task? (Y/N) ').upper()
        if rem_task == 'Y':
            rem_item = tasks.pop(0)
            print('Task removed!')
            print(f'Removed task: {rem_item}')
            continue
        elif rem_task == 'N':
            print('Successfully cancelled!')
            continue
        else:
            print('Please input Y/N!')
            continue
    elif option == 4:
        print('Goodbye!')
        exit()
    else:
        print('Try again!')
        continue