characters = []
nome = []
atq = []
defesa = []

for i in range(3):
    nome = input("Insira o nome: ")
    atq = int(input("Insira o ataque: "))
    defesa = int(input("Insira a defesa: "))
    characters.append([nome, (atq, defesa)])

for character in characters:
    print(character[0])
    print(character[1][0])
    print(character[1][1])
    
print(characters)
print("Ataque", max(characters, key = lambda x: x[1][0])[0], max([character[1][0] for character in characters]))
print("Defesa", max(characters, key = lambda x: x[1][1])[0], max([character[1][1] for character in characters]))