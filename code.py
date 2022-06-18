import PySimpleGUI as sg

table_content = []
layout = [
    [sg.Table(headings = ['Observation','Result'], values = table_content)]
]

window = sg.Window('Graph App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()