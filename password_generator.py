import PySimpleGUI as sg
import random
import string

sg.theme('Material2')

layout = [
    [sg.Text ('Tamanho da senha (Dígitos):', font='Montserrat 15'),
    sg.Input(size=(3, 1), font='Montserrat 15', key='tamanho')],
    [sg.Text('Senha', font='Montserrat 15')],
    [sg.InputText(size=(25, 1), font='Arial 28', pad=(0, (0, 10)), key='saida')],
    [sg.Button('Gerar', size=(8, 1), font='Arial 12'),
    sg.Button('Sair', size=(8, 1), font='Arial 12')]
]

tela = sg.Window('Safepassword', element_justification='center', layout=layout,
                  size=(500, 240), finalize=True)

#Tela Loop
while True:
    event, values = tela.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'Gerar' and values['tamanho'] == '':
        sg.popup('Informe o tamanho da senha!')
        continue

    elif event == 'Gerar':
        codificacao = string.ascii_letters + string.digits + '!@#$%&*+?/<>=(),;:.'
        rand = random.SystemRandom()
        tela['saida'].update(''.join(rand.choice(codificacao) for i in range(int(values['tamanho']))))
