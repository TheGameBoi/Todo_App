import streamlit as st
import functions

todos = functions.get_todos()

st.title('To-Do Webpage')
st.subheader("This is your To-Do List")
st.write("This app helps you stay organized!")

for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Enter a task...")