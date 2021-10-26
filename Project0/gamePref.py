games = ['stardew valley','valorant','overwatch','minecraft']

print("i like to play:")
print(*games, sep= ", ")
inputu = input("what game do you like? ")
games.append(inputu)
print("we like to play:")
print(*games, sep= ", ")