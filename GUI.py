import functions
# Third party library we have installed
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")
# layout expects a list
# each square braces separates hence added in diff list in layout
window = sg.Window('My Todo App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    # window. read() has two things, one is event and another value(which is dictionary)
    event, values = window.read()
    # print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            print(new_todo)
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

