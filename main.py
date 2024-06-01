todos = []
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
#

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        try:
            todo = user_action[4:]

            file = open('../Web_App1/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo + '\n')

            file = open('../Web_App1/todos.txt', 'w')
            file.writelines(todos)
        except ValueError:
            print("Invalid text. Must contain the number of the item, please try again.")
            continue

    elif user_action.startswith("show"):
        try:
            file = open('../Web_App1/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                row = f"{index + 1}. {item}"
                print(row)
        except ValueError:
            print("Invalid text. Must contain the number of the item, please try again.")
            continue

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            file = open('../Web_App1/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todo = input("Enter new to-do: ")
            todos[number] = new_todo + '\n'

            file = open('../Web_App1/todos.txt', 'w')
            file.writelines(todos)
        except ValueError:
            print("Invalid text. Must contain the number of the item, please try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            file = open('../Web_App1/todos.txt', 'r')
            todos = file.readlines()
            todo_complete = todos[number - 1].strip('\n')
            file.close()

            todos.pop(number - 1)

            file = open('../Web_App1/todos.txt', 'w')
            file.writelines(todos)
            message = f"{todo_complete} was completed from the list."
            print(message)
        except ValueError:
            print("Invalid text. Must contain the number of the item, please try again.")
            continue
        except IndexError:
            print('Invalid number. Please try again.')

    elif user_action.startswith("exit"):
        try:
            print("Goodbye.")
            break
        except ValueError:
            exit("Invalid text. Must contain the number of the item, please try again.")
            continue
    else:
        print("Command not valid.")
