import os
from math import gcd

p = './tests/'
cases = os.listdir(p)

proved = set() # guarda los numeros ya analizados por el algoritmo de 
               #fuerza bruta para en caso de repeticion terminar antes

def brute_force(a: int):
# busca todos los divisores de a y los compara dos a dos 
# para comprobar que ningun par cumple la condicion
    if a in proved:
        return True
    divisors = []
    div = 2
    while div * div <= a:
        if a%div == 0:
            divisors.append(div)
            if div*div != a:
                divisors.append(a//div)
        div = div+1
    if len(divisors)<2:
        proved.add(a)
        return True
    for i in range(1,len(divisors)):
        for j in range(i):
            if gcd(divisors[i]+divisors[j],a) == 1:
                return False
    proved.add(a)
    return True

def check_case(in_file, out_file):
    n = int(in_file.readline())
    a = list(map(int, in_file.readline().split()))
    d1_out = list(map(int, out_file.readline().split()))
    d2_out = list(map(int, out_file.readline().split()))
    
    #comprobando formato correcto
    if len(d1_out) != n or len(d2_out)!= n:
        False,'Wrong Answer'
    
    for i in range(n):
        if d1_out[i] == -1 or d2_out[i] == -1:
            if d1_out[i] != d2_out[i]:
                return False, 'Wrong Answer'
            # si la respuesta es -1 comprueba que no exista ningun par
            elif not brute_force(a[i]):
                return False, 'Wrong Answer'
        else: # si es distinta de menos -1, comprueba que d1 y d2 sean correctos
            if a[i]%d1_out[i]!=0 or a[i]%d2_out[i]!=0:
                return False, 'Wrong Answer'
            if gcd(d1_out[i]+d2_out[i],a[i]) != 1:
                return False, 'Wrong Answer'
    return True, 'Accepted'

for file in cases:
    name,extension  = os.path.splitext(file)
    if extension != '.out':
        continue
    input_file = open(p + name + '.in', 'r')
    output_file = open(p + name + '.out', 'r')
    check, judgement = check_case(input_file,output_file)
    print(f'{name} {judgement} ')
