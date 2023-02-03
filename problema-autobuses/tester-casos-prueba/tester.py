import os

p = './tests/'
cases = os.listdir(p)

def check_case(in_file, out_file):
    n,k,d = map(int,in_file.readline().split())  # parametros de entrada del caso
    lines = out_file.readlines()  #lineas de la respuesta del caso

    #Comprobacion del principio del palomar
    if n > k**d:
        if len(lines) > 1 or int(lines[0]) != -1:
            return False,'Wrong Answer. Expected -1'
        else:
            return True,'Accepted'

    if len(lines) != d:         # Si hay mas filas que dias
        return False,'Wrong Answer'
    
    mapping = []         # para eliminar los end_line('\n') de cada fila
    for i in range(len(lines)):
        line = lines[i][:-1].split()  #coge hasta la penultima posicion
        if len(line) != n:            #tiene que haber n columnas por cada fila
            return False,'Wrong Answer'
        mapping.append(line)
    
    
    students_distributions = set()   # para guardar las distribuciones de cada
                                    #alumno y comprobar que no hay 2 iguales

    for j in range(n):           #j las columnas
        distribution_i = []         #distribucion del alumno i-th
        for i in range(d):      # i las filas
            if int(mapping[i][j]) > k or int(mapping[i][j]) < 1:
                # los autobuses tienen denominacion 1<=m<=k
               return False,'Wrong Answer'
            distribution_i.append(mapping[i][j])   # agregar el dia jth del alumno ith
        distribution = ''.join(distribution_i) 
        #como cada representacion tiene que ser unica, 
        # comprobamos que no haya otra igual.
        if distribution in students_distributions:
            print(distribution)
            return False,'Wrong Answer'
        else:
            students_distributions.add(distribution)
    
    return True,'Accepted'

    
for file in cases:
    name,extension  = os.path.splitext(file)
    if extension != '.out':
        continue
    input_file = open(p + name + '.in', 'r')
    output_file = open(p + name + '.out', 'r')
    check, judgement = check_case(input_file,output_file)
    print(f'{name} {judgement} ')
