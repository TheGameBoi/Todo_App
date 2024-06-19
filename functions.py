todos = "todos.txt"

def get_todos(filepath=todos):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.read().splitlines(False)
    return todos_local

def write_todos(todos_arg, filepath=todos):
    with open(filepath, 'w') as file:
        file.write("\n".join(todos_arg))