class Quicksort():
    def sort(self, sequenza):
        # 🚨 1. CASO BASE (Terminazione)
        if len(sequenza)<=1: # Condizione uscita dalla ricorsione
            return sequenza
        else: # Faccio la ricorsione
            # 2. DIVIDI: Scelgo il pivot
            pivot = sequenza[0]

            # 3. Dividere la sequenza in sottoseq.
            sequenza_minori = []
            for i in range (1, len(sequenza)):
                if sequenza[i] < pivot:
                    sequenza_minori.append(sequenza[i])
                    
            # ⚠️ BEST PRACTICE: Usa la List Comprehension all'esame, è molto più sintetica!
            sequenza_maggiori = [n for n in sequenza if n > pivot]
            sequenza_uguali =  [n for n in sequenza if n == pivot]

            # 🚨 4. COMBINA (Impera): Chiamo sort() su sottoseq. e riassemblo
            return self.sort(sequenza_minori) + sequenza_uguali + self.sort(sequenza_maggiori)


qs = Quicksort()
sequenza = [3, 7, 11, 2, 5, 9, 4, 7]
sequenza_ordinata = qs.sort(sequenza)
print(sequenza_ordinata)
