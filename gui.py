import FreeSimpleGUI as sg

text = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="(Walk, Run, etc.)")
add_button = sg.Button("Add")
remove_button = sg.Button("Complete")
edit_button = sg.Button("Edit")
window = sg.Window('To-Do List', layout=[[text], [input_box], [add_button, edit_button, remove_button]])
window.read()
window.close()