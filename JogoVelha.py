import math
import random

Word = ["carapicuiba", "fernando", "abelha", "cor", "bola", "cunhado", "galinha", "cartao"]
randomWord = random.choice(Word)
valueWord = len(randomWord)

listWord = list(randomWord)
listGuess = ["_"] * valueWord

life = 6
letter = ""

while (life > 0) :
    print("a palavra possui {} de letras e {} de vidas \nadivinhe a palavra".format(valueWord, life))
    print(listGuess)
    letter = input("")
    for index, value in enumerate(listWord) :
        if value.lower == letter.lower :
            listGuess[index] = letter
    if not letter in listWord :
        life -= 1

    if listGuess == listWord :
        print("voce ganhou")
        break

else :
    print("voce perdeu")
           



