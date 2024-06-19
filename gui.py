import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("../Web_App1/todos.txt"):
    with open("../Web_App1/todos.txt", 'w') as file:
        pass

sg.theme("Green")
clock = sg.Text('', key='clock')
text = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="(Walk, Run, etc.)", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(25, 10))
add_button = sg.Button("Add")
remove_button = sg.Button("Complete")
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")

window = sg.Window('To-Do List', layout=[[clock], [text], [input_box], [add_button, [list_box, edit_button], remove_button], [exit_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=200)

    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case sg.WIN_CLOSED:
            print("Window Closed.")
            break

        case "Add":
            print("Executing Add")
            try:
                new_todos = values['todo']
                print(f"Adding: {new_todos!r}")
                todos = functions.get_todos()
                print(f"Loaded {len(todos)} todos")
                todos.append(new_todos)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Entry box cannot be blank.")
                continue

        case "Edit":
            print("Executing Edit")
            try:
                todo_to_edit = values['todos'][0]
                todo_to_edit.strip()
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Entry box cannot be blank.")
                continue

        case "Complete":
            print("Executing Complete")
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Entry box cannot be blank.")
                continue

        case "todos":
            print("Executing Todos")
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            print("Executing Exit")
            break

        case other:
            window["clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))

window.close()