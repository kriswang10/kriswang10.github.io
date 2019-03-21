from fractions import Fraction
import random
import cProfile
import time
def newint():
    sym=['+','-','×','÷']
    fh=random.randint(0,3)
    n1=random.randint(1,20)
    n2=random.randint(1,20)
    result=0
    if fh == 0:
        result=n1+n2
    elif fh == 1:
        n1,n2=max(n1,n2),min(n1,n2)
        result=n1-n2
    elif fh == 2:
        result=n1*n2
    elif fh == 3:
        n1,n2=max(n1,n2),min(n1,n2)
        while n1%n2 !=0:
            n1=random.randint(1,10)
            n2=random.randint(1,10)
            n1,n2=max(n1,n2),min(n1,n2)
        result=int(n1/n2)
    print(n1,sym[fh],n2,'=',end=' ')
    return result

def newfra():
    sym=['+','-','×','÷']
    fh=random.randint(0,3)
    t1=random.randint(1,10)
    t2=random.randint(t1,10)
    n1=Fraction(t1,t2)
    t1=random.randint(1,10)
    t2=random.randint(t1,10)
    n2=Fraction(t1,t2)
    result=0
    if fh == 0:
        result=n1+n2
    elif fh == 1:
        n1,n2=max(n1,n2),min(n1,n2)
        result=n1-n2
    elif fh == 2:
        result=n1*n2
    elif fh == 3:
        n1,n2=max(n1,n2),min(n1,n2)
        result=n1/n2
    print(n1,sym[fh],n2,'=',end=' ')
    return result

def newtest():
    sym=['+','-','×','÷']
    n=int(input())
    result=[]
    m=0
    while m<=(n-1):
        fh = random.randint(0,4)
        if fh ==0:
            print(m+1,end='、')
            result.append(newfra())
            print(' ')
        else:
            print(m+1,end='、')
            result.append(newint())
            print(' ')
        m = m + 1
    m=0
    print('答案:')
    while m <=(n-1):
          print(m+1,'、',result[m])
          m = m + 1


def main():
    print('1、四则运算')
    print('2、制作题库')
    n=int(input())
    if n == 1:      
        print('input"0000"to Quit')
        while True:
            fh = random.randint(0,4)
            if fh == 0:
                result=newfra()
                jg=input()
                if jg == '0000':
                    break;
                ans = Fraction(jg)
                if ans == result:
                    print('right')
                else:
                    print('error,the right answer is',result)
            else:
                result= newint()
                jg = input()
                if jg == '0000':
                    break;
                ans = Fraction(jg)
                if ans == result:
                    print('right')
                else:
                    print('error,the right answer is',result)
    if n==2:
        print('需要制作多少道题目：')
        newtest()

if __name__=='__main__':
    main()
          
