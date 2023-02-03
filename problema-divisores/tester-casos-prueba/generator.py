from random import randint

def generator_random(path:str, top_n = 500000,top_ai = 10000000):
    file = open(path,'w')
    n = randint(1,top_n)
    file.write('%d\n' %n)
    for i in range(n):
        ai = randint(2,top_ai)
        if i < n-1:
            file.write('%d ' %ai)
        else:
            file.write('%d\n' %ai)    
    file.close()
    print(f'{file.name} completed')
    

def generator_manual(path:str, n:int, a:list):
    file = open(path,'w')
    file.write('%d\n' %n)
    for i in range(n):
       if i < n-1: 
           file.write('%d ' %a[i])
       else:
           file.write('%d\n' %a[i]) 
    file.close()
    print(f'{file.name} completed')

if __name__ == "__main__":
    p = './tests/caso'
    generator_random(p+'1.in', 75000, 500000)
    #generator_random(p+'2.in')
    generator_random(p+'3.in', top_ai=700000)
    generator_manual(p+'4.in', 500000, [i+1 for i in range(500000)])
