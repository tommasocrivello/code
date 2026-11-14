from functools import lru_cache

class Fibonacci:
    def __init__(self):
        # ⚠️ CACHE MANUALE: Dizionario per ottimizzare la ricerca dei valori già calcolati
        self.cache = {} # cache{0 : 0, 1 : 1}
        self.cache[0] = 0
        self.cache[1] = 1

    # Mia funzione per il calcolo usando un dizionario
    def calcola_elemento_usando_cache(self, n): # Lo stato è in n
        if self.cache.get(n) is not None: # Se è già in cache
            return self.cache[n]
        else:
            self.cache[n] = (self.calcola_elemento_usando_cache(n-1) +
                             self.calcola_elemento_usando_cache(n-2))
            return self.cache[n]

    # 🚨 FONDAMENTALE: Decoratore Magico. Salva i calcoli intermedi automaticamente in memoria.
    # Usalo all'esame se l'algoritmo ricorsivo è troppo lento!
    @lru_cache(maxsize=None)
    def calcola_elemento(self, n): # Lo stato è in n
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.calcola_elemento(n-1)+self.calcola_elemento(n-2)

fib = Fibonacci()
print("Calcolo originariamente senza cache, ora ottimizzato con LRU-CACHE:")
value = fib.calcola_elemento(70)
print(value)
print("Calcolo usando cache:")
value = fib.calcola_elemento_usando_cache(70)
print(value)
