import PySimpleGUI as sg
import requests,json;

from PIL import Image

from translate import translate_text;
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Text("Text translator from english to russian language",font="Any 23",justification="center")],
            [sg.Text("Put only pdf file",font = "Any 20",justification="center",pad=((10,0),(0,50)))],
            [sg.Text("Enter a result pdf name:",font = "Any 18"),sg.InputText(size = (20,20))],
            [sg.Text("Enter font size:",font = "Any 15"),sg.InputText(key="font",size =(15,15))],
            [sg.InputText(key="-FILE_PATH-"),
            sg.FileBrowse("Open pdf")],
            [sg.Button('Translate'),sg.Button('Exit')],
            [sg.Text('',key = "connection",font = "Any 22",justification="center")]]

# Create the Window
window = sg.Window('Get image', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break;
    if event == "translate":
            address = values["-FILE_PATH-"];
            translate_text(20,address,"doc.docx");
print("Completed");
window.close();