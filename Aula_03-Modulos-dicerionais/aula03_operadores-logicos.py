#logica e (and)

verfica_email = True
verifica_senha = True

verifica_login = verfica_email and verifica_senha
print(verifica_login)

# Logica OU (or)
logica_ou = False or True
print(logica_ou)

#NOT
negacao = not True
print(negacao)

if not verifica_login:
    print("loga certo ai ...")
else:
    print("entra no programa")