#função com parametro sem retorno
def boas_vindas(nome):
    print(f"ola, {nome} seja bem-vindo!")

nome_digitado= input("digite seu nome")
boas_vindas(nome_digitado)

#função com parametro com retorno
def soma (num_a , num_b):
    soma = num_a + num_b
    return soma

print(soma(4,3))
print(type(nome_digitado))


resultado = soma(4,3)
print(resultado)
print(type(nome_digitado))
