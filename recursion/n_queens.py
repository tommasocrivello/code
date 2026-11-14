class NQueens:
    def __init__(self):
        self._num_solutions = 0
        self._solutions = [] # Qui memorizzo le soluzioni complete "buone" (valide)

    def solve_problem(self, N):
        # Chiamo la ricorsione la prima volta con
        # soluzione parziale vuota, ovvero una lista [ ]
        self._recursion([   ], N)

    def _recursion(self, partial_sol, N):
        # 🚨 1. CASO BASE (Condizione di Terminazione)
        if len(partial_sol) == N:
            # Prima di considerare buona (valida) una soluzione completa,
            # ovvero lunghezza di N, mi chiedo se per caso non
            # l'abbia già trovata prima (mi devo salvare le soluzioni)
            if self._solution_is_good(partial_sol):
                # NOTA: serve aggiungere .copy() qui in esecuzione reale per non sovrascrivere i reference!
                self._solutions.append(partial_sol.copy()) 
                print(partial_sol)
                self._num_solutions+=1
            return

        else :
            # 2. ESPLORAZIONE
            # partial_sol è una soluzione parziale, una lista di
            # tuple (r, c) che corrispondono a posizioni nella scacchiera
            for r in range(N):
                for c in range(N):
                    
                    # 🚨 3. SPORCO LO STATO (Aggiungo la mossa)
                    partial_sol.append(   (r,c)   ) # q_coords, coordinate della regina
                    
                    # 🚨 4. PRUNING (Verifica validità mossa appena fatta)
                    if self._pos_new_queen_is_acceptable(partial_sol):
                        # 🚨 5. RICORSIONE IN PROFONDITÀ
                        self._recursion(partial_sol, N) # Se non accettabile abortiamo la esplorazione
                    
                    # 🚨 6. BACKTRACKING (Pulisco lo stato)
                    partial_sol.pop() # Devo ricordarmi di togliere l'ultima regina
                                      # smontando così la soluzione costruita man mano
                                      # che le funzioni chiamate in modo ricorsivo ritornano

    # ⚠️ DA CAMBIARE ALL'ESAME: Logica specifica del problema per validare una mossa
    def _pos_new_queen_is_acceptable(self, partial_sol):
        last_queen = partial_sol[-1] # Ultima regina appena aggiunta
        for q in partial_sol[ : len(partial_sol)-1]: # Escludo l'ultima regina aggiunta
            if q[0] == last_queen[0]: # Stessa riga
                return False # Non ammissibile
            if q[1] == last_queen[1]: # Stessa colonna
                return False # Non ammissibile
            if q[0]-last_queen[1] == q[1]-last_queen[0]: # Stessa diagonale
                return False # Stessa diagonale
            if q[0]+last_queen[1] == q[1]+last_queen[0]: # Stessa diagonale (altra dir.)
                return False # Stessa diagonale
        return True # Non dimenticare di restituire True

    # ⚠️ DA CAMBIARE ALL'ESAME: Logica per scartare i duplicati
    def _solution_is_good(self, new_solution):
        for sol in self._solutions:
            for q in new_solution:
                if q in sol:
                    return False
        return True # Non dimenticare di restituire True


if __name__ == "__main__":
    nq = NQueens()
    nq.solve_problem(4)
    print(f"Num. solutions: {nq._num_solutions}")
