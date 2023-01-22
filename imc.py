import PySimpleGUI as sg

def calculo_imc(peso, altura):
    peso = int(peso.strip())
    altura = float(altura.strip())
    return round(peso / (altura ** 2), 1)

sg.theme('DarkBlue13')
layout = [
    [sg.Text('Peso:')],
    [sg.Input(key='peso')],
    [sg.Text('Altura:')],
    [sg.Input(key='altura')],
    [sg.Button('OK'), sg.Button('Cancelar')],
    [sg.Text('', key='imc')]
]

janela = sg.Window('Índice de Massa Corporal (IMC)', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    elif evento == 'OK':
        imc = calculo_imc(valores['peso'], valores['altura'])
        # Classifição do imc
        if (imc < 18.5):
            classificacao = 'Está abaixo do peso'
        elif (imc >= 18.5) and (imc <= 24.9):
            classificacao = 'Peso normal'
        elif (imc >= 25) and (imc <= 29.9):
            classificacao = 'Sobrepeso'
        elif (imc >= 30) and (imc <= 34.9):
            classificacao = 'Obesidade Grau I'
        elif (imc >= 35) and (imc <= 39.9):
            classificacao = 'Obesidade Grau II'
        else:
            classificacao = 'Obesidade Grau III ou Mórbida'
        janela['imc'].update(f'O seu IMC é {imc}\n{classificacao}')
        
janela.close()