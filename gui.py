import functions
import FreeSimpleGUI as sg


text = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="(Walk, Run, etc.)", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[25, 10])
add_button = sg.Button("Add")
remove_button = sg.Button("Complete")
edit_button = sg.Button("Edit")


window = sg.Window('To-Do List', layout=[[text], [input_box], [add_button, [list_box, edit_button], remove_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()