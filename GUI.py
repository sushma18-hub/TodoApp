import functions
# Third party library we have installed
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
# layout expects a list
# each square braces separates hence added in diff list in layout
window = sg.Window('My Todo App',layout=[[label],[input_box,add_button]])
window.read()
window.close()