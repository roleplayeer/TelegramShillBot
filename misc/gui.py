import PySimpleGUI as sg

sg.theme('Reddit')
layout = [  [sg.Text('Enter TG Code'), sg.InputText()],


            [sg.Button('Ok'), sg.Button('Cancel')] ]


window = sg.Window('Telegram Shill Bot', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

window.close()
