from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

num1 = 4
num2 = 2

print(type(num1), type(num2))

resultado = num1 // num2
print(resultado, type(resultado))


#atribuição
num = 15
print() #pular uma linha
print(num)

num += 2
print(num)


#operadores relacionais
print()
print(6 < 2)

idade = 21

print(idade >= 21)


logado = True
print(logado, type(logado))


maior_idade = idade >=18
print(maior_idade, type(maior_idade))


#string
nome1 = "Marcos"
nome2 = "marcos"

print(nome1.upper() == nome2.upper())