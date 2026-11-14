from time import sleep

# Contare da 10 a 1 in maniera ricorsiva
def countdown(n):
    # 🚨 CASO BASE
    if n==0:
        return # Esco dalla ricorsione
    # 🚨 PASSO RICORSIVO
    else:
        print(n)
        sleep(1)
        print(f"Chiamo la funzione con {n-1}")
        countdown(n-1)
        print(f"Esco dalla funzione") # Questa riga stampa solo in fase di srotolamento (backtracking)

countdown(10)
print("Finito il programma")
