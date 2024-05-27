import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title('To-Do Webpage')
st.subheader("This is your To-Do List")
st.write("This app helps you stay organized!")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a task...",
              on_change=add_todo, key='new_todo')
