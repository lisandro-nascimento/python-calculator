# ================================================

## Operador condicional

# 0-16 anos não pode
# 16-17 pode 50tinha ifood
# 18+ pode tirar CNH

idade = 111

if idade < 16:
    print("Não pode tirar CNH")
elif idade <=17:
    print("Pode 50tinha Ifood")
else:
    print("Pode Tirar CNH")


# ================================================

## Operador logico OR, AND e NOT

a = True
b = False

# AND as        DUAS condicoes PRECISAM ser VERDADEIRAS para o resultado ser VERDADEIRO
# OR UMA das    DUAS condicoes PRECISAM ser VERDADEIRAS para o resultado ser VERDADEIRO
# NOT           APENAS INVERTE O RESULTADO

print("a: ", a)                     # True
print("b: ", b)                     # False
print("=====================")      
print("a E b"   , a and b)          # False
print("a OU b"  , a or b)           # True
print("NOT a"   , not a)            # False
print("NOT b"   , not b)            # True


