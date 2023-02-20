import functions
# Third party library we have installed
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")
# Getting the values in todos and making it a list
list_box = sg.Listbox(values=functions.get_todos(),key="item",enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
# layout expects a list
# each square braces separates hence added in diff list in layout
window = sg.Window('My Todo App',
                   layout=[[label], [input_box, add_button],[list_box,edit_button]],
                   font=('Helvetica', 20))

while True:
    # window. read() has two things, one is event and another value(which is dictionary)
    event, values = window.read()
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            print(new_todo)
            todos.append(new_todo)
            functions.write_todos(todos)
            window['item'].update(values=todos)
        case "Edit":
            todo_to_edit = values["item"][0]
            updated_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = updated_todo
            functions.write_todos(todos)
            window['item'].update(values=todos)
        # key of the list box is used
        case 'item':
            window['todo'].update(value=values['item'][0])
        case sg.WINDOW_CLOSED:
            break

