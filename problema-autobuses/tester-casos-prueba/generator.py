from random import randint

def generator_random(path:str):
    file = open(path,'w')
    n = randint(1,1000)
    d = randint(1,1000)
    k = randint(1,int(1e9))
    file.write('%d %d %d\n' %(n,k,d))
    file.close()
    

def generator_manual(path:str, n:int, k:int, d:int):
    file = open(path,'w')
    file.write('%d %d %d\n' %(n,k,d))
    file.close()
    print(f'{file.name} completed')

if __name__ == "__main__":
    p = './tests/caso'
    #generator_manual(p+'1.in',1,1,1)
    #generator_manual(p+'2.in',27,3,3)
    #generator_manual(p+'3.in',1000,int(1e9),1000)
    #generator_manual(p+'4.in',65,4,3)
    #generator_manual(p+'5.in',64,4,3)
    generator_manual(p+'6.in',124, 6, 5)
