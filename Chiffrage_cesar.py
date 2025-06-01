#Crée le 2025-05-28 à 23h59, fini le 2025-05-30 à 13h43
#Algorithm de chiffrage en code César

cle= int(input("choisis ta clé:"))
message=input(str("Écrivez votre message codé:"))
message_min=message.lower()
remplace_accent = {224: 97, 225: 97, 226: 97, 231: 99, 232: 101, 233: 101, 234: 101, 235: 101, 238: 105, 239: 105,
                   244: 111, 246: 111, 249: 117, 251: 117, 252: 117}
messageF=message_min.translate(remplace_accent)


def chifferage_cesar(messageF):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    taille= len(alphabet)
    listeCara = []
    for caractere in messageF:
        if caractere in alphabet:
            index= alphabet.index(caractere)
            nouveau_index= (index + cle)% taille
            listeCara.append(alphabet[nouveau_index])
        else:
            listeCara.append(caractere)

    message_chiffre= "".join(listeCara)
    print(f"Voici le message chiffré avec une clé valant {cle:}: {message_chiffre}")

chifferage_cesar(messageF)

