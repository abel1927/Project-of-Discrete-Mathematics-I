from sys import stdin,stdout

# n = cantidad de alumnos
# d = cantidad de días
# k = cantidad de autobuses 
n, k, d  = map(int, stdin.readline().split())

def pow(base,exp):
    b = base
    while exp>1:
        exp = exp-1
        b = b*base
    return b

# Principio del palomar:
# Si hay mayor cantidad de alumnos que posibles asignaciones distintas de 
# autobuses por días, entonces al menos 2 alumnos tendrán la misma 
# asignación por lo cual se harán amigos luego de los d días.
if n > pow(k,d):
    stdout.write('-1\n')
    exit(0)
 
answer = [['1' for i in range(n)] for j in range(d)]
distribution = [1 for i in range(d)]
for i in range(1,n):
    for j in range(d-1,-1,-1):
        distribution[j] = (distribution[j]%k + 1)
        if distribution[j] != 1: 
            break
    for j in range(d):
        answer[j][i] = str(distribution[j])

for row in answer:
    stdout.write(' '.join(row)+'\n')
