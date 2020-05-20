nome = str(input("Digite seu nome: "))

print(f"\nAlô {nome}, voçe gostaria de aprender um pouco de Python hoje?")

print(f"\nMinuscula: {nome.lower()}, Maiuscula: {nome.upper()}, Primeira Maiuscula: {nome.title()}")

mensagem = '\nAlbert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo"'
print(mensagem) #era pra estar em italico

famous_person = str(input("\nDigite o nome do autor:\n\t"))
mensagem2 = print("\nO autor famoso é o(a) {}\n" .format(famous_person))


print(famous_person)
print(famous_person.lstrip())
print(famous_person.rstrip())
print(famous_person.strip())

