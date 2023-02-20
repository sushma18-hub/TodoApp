from zipcreator import make_archive
import PySimpleGUI as sg
import pathlib
label_1 = sg.Text("Select files to compress")
input_box_1 = sg.InputText(tooltip="Enter Files")
add_button_1 = sg.FilesBrowse("Choose", key="files")

label_2 = sg.Text("Select destination folder")
input_box_2 = sg.InputText(tooltip="Enter destination folder")
add_button_2 = sg.FolderBrowse("Choose", key="folder")

add_button_3 = sg.Button("Compress")
finished = sg.Text(key="output",text_color="green")
window = sg.Window('File Zipper',layout=[[label_1,input_box_1,add_button_1],[label_2,input_box_2,add_button_2],[add_button_3,finished]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Files are compressed successfully")

window.close()

