import PySimpleGUI as sg

sg.theme('Dark')
table_content = []
layout = [
    [sg.Table(
        headings = ['Observation','Result'],
        values = table_content,
        expand_x = True,
        hide_vertical_scroll = True,
        key = '-TABLE-')],
    [sg.Input(key = '-INPUT-', expand_x = True), sg.Button('Sumbit')],
    [sg.Canvas(key = '-CANVAS-')]
]

window = sg.Window('Graph App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Sumbit':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1,float(new_value)])
            window ['-TABLE-'].update(table_content)
            window ['-INPUT-'].update('')

window.close()