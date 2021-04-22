dicPC={"HP": 11 , "Acer": 7 , "Lenovo": 17 , "Del": 23}
dicPhone={"Sumsung": 22 , "Iphone": 9 , "Other": 13 }
dicTablette = {"Sumsung": 15 , "Other": 13}

dicTotal = {}
# Premier méthode avec la boucle FOR
for i in [dicPC , dicPhone, dicTablette]:
    dicTotal.update(i)

print(dicTotal)
print("")

# Deuxieme méthode avec la méthode UPDATE
dicTotal.update(dicPC)
dicTotal.update(dicPhone)
dicTotal.update(dicTablette)

print(dicTotal)
