from time import time
import scipy

c = 0

def binomial(n, m):
    # 🚨 CASO BASE
    if m==n or m==0: #(n n) = 1, (n 0) =1
        return 1
    # 🚨 PASSO RICORSIVO TRIPLO (Divide l'albero in rami)
    else:
        global c # ⚠️ Cattiva pratica usare variabili globali, il prof l'ha fatto solo per test!
        c = c+1
        return binomial(n-1, m-1)+binomial(n-1, m)


start_time = time()
b = binomial(50, 7)
print(f"Il binomiale vale: {b}")
#print(f"Numero di chiamate della funzione: {c}")
end_time = time()
print(end_time-start_time)

start_time = time()
b = scipy.special.binom(200, 20)
print(f"Il binomiale vale: {b}")
end_time = time()
print(end_time-start_time)
