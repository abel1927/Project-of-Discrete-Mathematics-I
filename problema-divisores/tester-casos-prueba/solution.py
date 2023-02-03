from sys import stdin,stdout

max_n = 10**7+1
# precomputar el minimo factor primo de cada numero en el rango max_n
# si es 0 es que no ha sido actualizado, al final quedaran en 0 los primos
min_prime = [0 for _ in range(max_n)]

# siguiendo el funcionamiento del algoritmo de la Criba de Eratostenes
# marcaremos los numeros como primos(quedando un 0) y como no primos 
# dejando en la posicion del numero el menor primo que lo divide que es por el 
# que fue alcanzado durante la ejecucion de la criba
def sieve_e(n): 
    p = 2
    while p * p <= n:
        if not min_prime[p]: # si es primo buscamos sus multiplos no analizados
            for i in range(p*p, n, p):
                # si en este momento estaba marcado como primo y es multiplo de p
                # entonces p es el menor primo que lo divide
                if not min_prime[i]: 
                    min_prime[i] = p
        p = p + 1

sieve_e(max_n)

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

d1 = ['-1' for _ in range(n)]
d2 = ['-1' for _ in range(n)]

for i in range(n):
    p = min_prime[a[i]] # seleccionamos el min factor primo de ai
    if p != 0:   # si esta marcado como 0, ai es primo y no posee a d1,d2
        while a[i] % p == 0: 
        # 'extraemos' de ai todas las ocurrencias de p. ( exponente 
        # en la descomposicion) 
            a[i] = a[i]//p
        # si ai se hace 1, su descomposion es de la forma p^k y tiene a p
        # como unico factor primo, luego no tiene d1,d2
        if a[i] > 1:
        # si ai > 1 posee al menos un factor primo distinto de p
            d1[i], d2[i] = str(p), str(a[i])

stdout.write(' '.join(d1)+'\n')
stdout.write(' '.join(d2))
