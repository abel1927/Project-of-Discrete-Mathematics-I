from sys import stdin,stdout

# n = cantidad de alumnos
# d = cantidad de días
# k = cantidad de autobuses 
n, k, d  = map(int, stdin.readline().split())

# Principio del palomar:
# Si hay mayor cantidad de alumnos que posibles asignaciones distintas de 
# autobuses por días, entonces al menos 2 alumnos tendrán la misma 
# asignación por lo cual se harán amigos luego de los d días.
if n > k**d:
    stdout.write('-1\n')
    exit(0)
 
answer = [['1' for i in range(n)] for j in range(d)]
distribution = [1 for i in range(d)]
for i in range(1,n):
    for j in range(d-1,-1,-1):
      #los restos mod(k) son [0,1,..,k-1], con lo cual al sumar 1 se garantiza
      # que el valor en j esta en [1,..,k] que son las denominaciones de los autobuses 
        distribution[j] = (distribution[j]%k + 1) 
     # si se hace 1, es porque %k = 0, con lo cual habia llegado a 5 y cubierto todos los
     # valores para la posicion j manteniendo fijas las restantes hasta j-1
        if distribution[j] != 1: 
            break
    for j in range(d):
        answer[j][i] = str(distribution[j])

for row in answer:
    stdout.write(' '.join(row)+'\n')
