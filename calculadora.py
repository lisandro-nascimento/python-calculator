# Develop a calculator with the operations: add, subtract, divide and multiply
# The calculator should work this way:
# 1 - Receive an input from user specifying wich operation the calculator should perform:
#      1 - add
#      2 - subtract
#      3 - divide
#      4 - multiply
# Note: You should validate that the user passed only an available option, returning an error in case
#       He passed any unavaible option. If user pass an unvailable option, run this: raise Exception("Opcao invalida, escolha um numero de 1-4")
# 2 - Require two numbers from user which will be stored on variables 'a' and 'b' respectively
# 3 - According to users inputs (operation and parameters) perform the required operation and print the result

operador = int(input('Escolha um dos operadores abaixo:' 
                     '\n1 - add ' 
                     '\n2 - subtract '
                     '\n3 - divide ' 
                     '\n4 - multiply: \n'
                     'Digite um operador: '))
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

def resultado(a:int, b:int) -> int:
    if operador == 1:
        return a + b
    elif operador == 2:
        return a - b
    elif operador == 3:
      return a / b
    elif operador == 4:
      return a * b
    else:
        raise Exception('Opcao invalida, escolha um numero de 1-4')

print("Resultado: ", resultado(a, b))