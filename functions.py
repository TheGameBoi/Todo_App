file = open('todos.txt', 'r')
todos = file.readlines()
file.close()

file = open('todos.txt', 'w')
file.writelines(todos)
