class Anagrams:
    def __init__(self):
        pass

    def recursion(self, anagramma_parziale, lettere_rimanenti):
        # 🚨 1. CASO BASE (Condizione di Terminazione)
        if len(lettere_rimanenti)==0: # Finito le lettere
            print(anagramma_parziale)
        else:
            # 2. ESPLORAZIONE
            for i in range(len(lettere_rimanenti)):
                
                # 🚨 3. SPORCO LO STATO (Aggiungo)
                anagramma_parziale += lettere_rimanenti[i]
                
                # Passo lo stato aggiornato ai figli
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                
                # 🚨 4. RICORSIONE IN PROFONDITÀ
                self.recursion(anagramma_parziale, nuove_lettere_rimanenti)
                
                # 🚨 5. BACKTRACKING (Pulisco lo stato)
                # Tolgo esattamente l'ultima lettera che avevo appena aggiunto
                anagramma_parziale = anagramma_parziale[:-1]

anagram = Anagrams()
anagram.recursion("", "dog")
