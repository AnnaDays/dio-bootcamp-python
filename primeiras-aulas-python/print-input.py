nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n") #adiciona 3 pontos no final e quebra linha
print(nome, idade, sep="#", end="...\n") #adiciona no meio do nome uma hashtag, 3 pontos no final e quebra linha 
print(nome, idade, sep="#") #adiciona uma hashtag no meio