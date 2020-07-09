def header(msg):
    print('=' * 30)
    print(f'  {msg}')
    print('=' * 30)


def calculadora(imc):
    from time import sleep
    imc = peso / (altura ** 2)
    print('\nHumm...Vejamos\n')
    sleep(1)
    print(f'Seu IMC é:\033[1;30m {imc:.1f}\033[m')
    if imc < 18.5:
        print(f'Você está abaixo do peso, {nome}!!')
    elif imc < 25:
        print(f'Você está com o peso ideal, {nome}.')
    elif imc < 30:
        print(f'Você está com sobrepeso, {nome}.')
    elif imc < 40:
        print(f'Você está com obesidade, {nome}!')
    else:
        print(f'Você está com obesidade mórbida, {nome}!!')


header(f'''\033[1;31m{"CALCULADORA DE IMC":^25}\033[m 
\033[1;32m{"Índice de Massa Corporal":^30}\033[m''')
nome = str(input('\nOlá! Como se chama? ')).capitalize().strip()
peso = float(input(f'Tudo bem, {nome}? Qual o seu peso atual? '))
altura = float(input('Ótimo! Agora me diga sua altura:[x.xx] '))
calculadora(peso)
# calculadoraIMC
