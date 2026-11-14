# Verifico se parola palinroma
# (per semplicità lunghezza dispari)

def is_palindrome(word):
    # 🚨 CASO BASE
    if len(word) == 1:
        return True # Se sono arrivato qui, è palindroma
    else: # Se la lettera iniziale e finale sono uguali ...
        # 🚨 RICORSIONE: Richiama se stessa accorciando lo stato (taglia primo e ultimo carattere)
        return word[0] == word[-1] and is_palindrome(word[1:-1]) # Sottostringa da 1 a len-1

parola = input("Parola: ")
result = is_palindrome(parola)
print(result)
