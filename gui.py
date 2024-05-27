import functions
import FreeSimpleGUI as sg


text = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="(Walk, Run, etc.)", key="to-do")
add_button = sg.Button("Add")
remove_button = sg.Button("Complete")
edit_button = sg.Button("Edit")

window = sg.Window('To-Do List', layout=[[text], [input_box], [add_button, edit_button, remove_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['to-do'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)


window.close()