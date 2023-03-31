from collections import deque
import sys
import copy
from heapq import heappop,heappush,heapify
import math

def bj_12865():
    n,k=map(int,input().split())
    w_v=[list(map(int,input().split())) for _ in range(n)]
    d_p_map=[0 for _ in range(k+1)]
    for i in range(n):
        tmp=[0 for _ in range(k+1)]
        for j in range(1,k+1):
            weight,value=w_v[i]
            if j-weight<0:
                tmp[j]=d_p_map[j]
            else:
                tmp[j]=max(d_p_map[j-weight]+value,d_p_map[j])
        d_p_map=tmp   
    return d_p_map[-1]
# print(bj_12865())

def bj_1655():
    n=int(input())
    left_list=[]
    right_list=[]
    result=[]
    for i in range(n):
        num=int(sys.stdin.readline())
        heappush(right_list,num)
        tmp_num=heappop(right_list)
        heappush(left_list,(-tmp_num,tmp_num))
        if len(left_list)-len(right_list)>1:
            heappush(right_list,heappop(left_list)[1])
        result.append(left_list[0][1])

    return result
# result=bj_1655()
# for num in result:
#     print(num)

def bj_3197():
    n,c=list(map(int,input().split()))
    before_maps=[[] for _ in range(n)]
    for i in range(n):
        before_maps[i]=list(sys.stdin.readline().rstrip())
        for j in range(c):
            if before_maps[i][j]=='L':
                L_x_y=(i,j)
                break
    meet=False
    day=0
    x_offset=[1,-1,0,0]
    y_offset=[0,0,1,-1]
    while meet==False and day<=n*c:
        to_do_list=deque()
        to_do_list.append(L_x_y)
        visited=[[False for _ in range(c)] for _ in range(n)]
        visited[L_x_y[0]][L_x_y[1]]=True
        while len(to_do_list)>0 and meet==False:
            do=to_do_list.popleft()
            indexes=[(do[0]+x_offset[index],do[1]+y_offset[index]) for index in range(4)]
            for x,y in indexes:
                if 0<=x and x<n and 0<=y and y<c and visited[x][y]==False:
                    if before_maps[x][y]=='.':
                        to_do_list.append((x,y))
                        visited[x][y]=True
                    if before_maps[x][y]=='L':
                        meet=True
                        return day
        
        after_maps=copy.deepcopy(before_maps)
        for i in range(n):
            for j in range(c):
                indexes=[(i+x_offset[index],j+y_offset[index]) for index in range(4)]
                if before_maps[i][j]=='X':
                    for x,y in indexes:
                        if 0<=x and x<n and 0<=y and y<c and (before_maps[x][y]=='.' or before_maps[x][y]=='L'):
                            after_maps[i][j]='.'
                            break
        before_maps=after_maps
        day+=1
        
    return -1

# print(bj_3197())

def factorial(num,p):
    fac=1
    for i in range(1,num+1):
        fac=fac*i%p
    return fac

def power(num,p,mod):
    if p==1:
        return num%mod
    if p%2==0:
        return (power(num,p//2,mod)**2)%mod
    else:
        return ((power(num,p//2,mod)**2)*num)%mod
    
def bj_11401():
    n,k=list(map(int,sys.stdin.readline().rstrip().split()))
    p=1000000007
    return (factorial(n,p)*power((factorial(k,p)*factorial(n-k,p))%p,p-2,p))%p
# print(bj_11401())


def array_mul(a,b,n):
    result=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum=0
            for k in range(n):
                sum=sum+a[i][k]*b[k][j]
            result[i][j]=sum%1000
    return result
def power(array,B,N):
    if B==1:
        return array
    array_B=power(array,B//2,N)
    if B%2==0:
        return array_mul(array_B,array_B,N)
    else:
        return array_mul(array_mul(array_B,array_B,N),array,N)
def bj_10830():
    N,B=list(map(int,input().split()))
    A=[list(map(lambda x:int(x)%1000,input().split())) for _ in range(N)]
    return power(A,B,N)
# result=bj_10830()
# for array in result:
#     print(" ".join(map(str,array)))

def array_mul_pibo(a,b):
    result=[[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            sum=0
            for k in range(len(b)):
                sum=sum+a[i][k]*b[k][j]
            result[i][j]=sum%1000000
    return result

def power_pibo(array,B):
    if B==1:
        return array
    array_B=power_pibo(array,B//2)
    if B%2==0:
        return array_mul_pibo(array_B,array_B)
    else:
        return array_mul_pibo(array_mul_pibo(array_B,array_B),array)

def bj_2749():
    n=int(input())
    init_array=[[1,1],[1,0]]
    factor_array=power_pibo(init_array,n)
    return array_mul_pibo(factor_array,[[1],[0]])[1][0]
# print(bj_2749())
# print(array_mul_pibo([[1,2],[3,4]],[[1,2],[3,4]]))

def bj_11066():
    t=int(sys.stdin.readline())
    result=[]
    for i in range(t):
        n=int(sys.stdin.readline())
        num_list=[0]+list(map(int,sys.stdin.readline().rstrip().split()))
        dp_list=[[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(n,0,-1):
            for j in range(i+1,n+1):
                page_list=[dp_list[i][k]+dp_list[k+1][j] for k in range(i,j)]
                dp_list[i][j]=min(page_list)+sum(num_list[i:j+1])

        result.append(dp_list[1][n])
    return result

result=bj_11066()
for min_cost in result:
    print(min_cost)
# f(1,2)->f(1,1)+f(2,2)
# f(1,3)->f(1,1)+f(2,3)
#         f(1,2)+f(3,3)
# f(1,4)->f(1,1)+f(2,4)
#         f(1,2)+f(3,4)
#         f(1,3)+f(4,4)
#     A B C D
# A   
# B
# C
# D
