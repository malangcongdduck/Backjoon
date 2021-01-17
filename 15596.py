'''
def solve(a):
    return sum(a)
'''

def func_sum(a):
    result=0
    for i in range(len(a)):
        result+=a[i]
    return result

if __name__ == "__main__":
    n=int(input())
    a=[None]*n
    a=list(map(int,input().split()))
    print(f'{func_sum(a)}') 
