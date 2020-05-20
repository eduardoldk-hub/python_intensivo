pessoa = str(input("Digite um valor: "))
# .strip remove os espaços da inserção, lstrip(), remove os espaços do lado direito
pessoa = pessoa.strip()

if pessoa == 'eduardo':
    print("imprimiu sem os espaços")
else:
    print("nao imprimiu")