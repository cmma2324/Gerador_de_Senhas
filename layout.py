import PySimpleGUI as sg
from senha import gerador_de_senha

Layout = [
    [sg.Text('Quantidade de Caracteres')],
    [sg.InputText()],
    [sg.Text('Sua senha é: ', key='senha')],
    [sg.Button('Gerar senha')],
    [sg.Text('')],
]

janela = sg.Window('Gerador de Senhas', Layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Gerar senha':
        senha = gerador_de_senha(int(valores[0]))
        janela['senha'].update(f'Sua senha é: {senha}')
    

janela.close()