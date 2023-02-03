from sys import stdin,stdout
from math import gcd

def solveTest(a,m):
    count=0
    d = gcd(a,m)
    for x in range(m):
        if gcd(a+x,m) == d:
            count = count+1
    return count

if __name__ == "__main__":
    T = int(stdin.readline())
    answer = []
    for _ in range(T):
        a,m = map(int,stdin.readline().split())
        answer.append(str(solveTest(a,m))+'\n')
    stdout.write(''.join(answer))
