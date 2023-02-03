from sys import stdin,stdout

n = 0           # n: cantidad de vertices y aristass
visited = []     #para el dfs de detectar el ciclo
visited2 = []   #para el dfs de contar los vertices de los subarboles 
stack = []       #para ir guardando los vertices en el recorrido en profundidad
                 # y saber los vertices que integran el ciclo
cycle_vertex = []  # para almacenar los vertices que forman el ciclo


def  buildGraph():         # para leer el grafo de cada test
    global n,visited,visited2,cycle_vertex,stack
    n = int(stdin.readline())
    visited = [False for i in range(n)]
    visited2 = [False for i in range(n)]
    cycle_vertex = []
    stack = []
    G = [[] for i in range(n)]
    for _ in range(n):
        u,v = map(int,stdin.readline().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    return G

def detect_cycle_dfs(G,v,pv): 
#G: grafo, v el vertice , pv padre de v en el recorrido en profundidad
    global visited
    visited[v] = True
    stack.append(v) # va "contruyendo la rama" que se analiza en el recorrido
    for u in G[v]:
        #detectar la arista de retroceso que crea el ciclo
        if visited[u] and u!= pv:
            # <u,p(u),p(p(u))....,u> forman el ciclo
            while stack[-1] != u:
                c_v = stack.pop()
                cycle_vertex.append(c_v)
                visited2[c_v] = True
            cycle_vertex.append(u)
            visited2[u] = True
            return True # para detener la recursion
        elif not visited[u]:
            if detect_cycle_dfs(G,u,v):
                return True  # para detener la recursion
    stack.pop() # va "deshaciendo la rama"
    return False

#cv : vertice de ciclo
count_cv = 0  # almacena la cantidad de vertices en el arbol de cv

def count_dfs(G,v,pv):
#G: grafo, v el vertice , pv padre de v en el recorrido en profundidad
    global count_cv,visited2
    count_cv = count_cv + 1
    visited2[v] = True
    for u in G[v]:
        if not visited2[u]:
            count_dfs(G,u,v)
    
def solve():
    global count_cv,n
    t = int(stdin.readline())    #cantidad de test
    answer = []
    while t > 0:
        t = t-1
        G = buildGraph()
        detect_cycle_dfs(G,0,0)
        total_paths = 0             # almacena el total de caminos simples
        for cv in cycle_vertex:
            count_cv = 0
            count_dfs(G,cv,cv)
            #total_cv : sumando correspondiente de la sumatoria
            total_cv = (count_cv*(count_cv-1))//2 + count_cv*(n-count_cv)
            total_paths = total_paths + total_cv
        answer.append(str(total_paths)+'\n')
    stdout.write(''.join(answer))

if __name__ == "__main__":
    solve()


