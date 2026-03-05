# Crie uma funcao que receba a idade e o sexo de uma pessoa e essa funcao informe se ela precisa
# se alistar no exercito pras guerras que o trump ta arrumando por ai de acordo com a regra abaixo:
# Se for homem maior de 18 anos, deve se alistar

idade = 19
sexo = 'F'


def deve_alistar(idade:int, sexo:str):
    if idade > 18 and sexo == 'M':
        print('você pode se alistar')
    else:
        print('voce não pode se alistar')
resultado = deve_alistar(idade, sexo)
    