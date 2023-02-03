from sys import stdin,stdout


def gcd_e(a,b): #Algoritmo de euclides para el calculo del mcd
    while b != 0:
        b, a = a % b, b
    return a

def phi(m):   #Calcular el valor de phi(m) usando la factorizacion de m
    phi_m = m  # Almacenar el valor de phi(m)
    div = 2      # marca los divisores
    while div*div <= m:      
        if m % div == 0:
            while m % div == 0:  # todas las ocurrencias(exponente) en 
                m = m//div       # la descomposicion
            phi_m = phi_m - phi_m//div
        div = div + 1
    #un numero tiene a lo sumo 1 divisor mayor que su raiz    
    if m > 1:
        phi_m = phi_m - phi_m//m
    return phi_m

def solve():
    T = int(stdin.readline())
    answer = []
    for _ in range(T):
        a,m = map(int,stdin.readline().split())
        d = gcd_e(m,a)
        answer_i = phi(m//d)
        answer.append(str(answer_i)+'\n')
    stdout.write(''.join(answer))

if __name__ == "__main__":
    solve()