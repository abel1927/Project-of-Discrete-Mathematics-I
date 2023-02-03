from random import randint

def generator_random(path:str, top_T=50,top_m = 10000000000):
    file = open(path,'w')
    T = randint(1,top_T)
    file.write('%d\n' %T)
    for _ in range(T):
        m = randint(2,top_m)
        a = randint(1,m-1)
        file.write('%d %d\n' %(a,m))
    file.close()
    print(f'{file.name} completed')
    

def generator_manual(path:str, T:int, a:list, m:list):
    file = open(path,'w')
    file.write('%d\n' %T)
    for i in range(T):
       file.write('%d %d\n' %(a[i],m[i])) 
    file.close()
    print(f'{file.name} completed')

def fibonacci_case(path:str):
    file = open(path,'w')
    file.write('30\n')
    f = [1,2]
    for i in range(2,32):
        f2,f1 = f[i-2],f[i-1]
        file.write('%d %d\n' %(f2,f1))
        f.append(f2+f1)
    file.close()
    print(f'{file.name} completed')

if __name__ == "__main__":
    p = './tests/caso'
    #generator_manual(p+'1.in',5,[7,14,11,11,13],[13,23,19,12,21])
    fibonacci_case(p+'9.in')
    #generator_random(p+'10.in', top_m=1377779)  
