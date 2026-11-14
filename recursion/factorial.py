def factorial(n):
    # 🚨 CASO BASE
    if n==0 or n==1:
        return 1
    # 🚨 PASSO RICORSIVO
    else:
        return n*factorial(n-1)

num = 100
f = factorial(num)
print(f"Fattoriale di {num}: {f}")
