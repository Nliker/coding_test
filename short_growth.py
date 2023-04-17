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

# result=bj_11066()
# for min_cost in result:
#     print(min_cost)
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

def bj_11049():
    n=int(input())
    array_list=[0]+[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
    dp_list=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n,0,-1):
        for j in range(i+1,n+1):            
            dp_list[i][j]=min([dp_list[i][k]+dp_list[k+1][j]+(array_list[i][0]*array_list[k][1]*array_list[j][1]) for k in range(i,j)])
    return dp_list[1][n]
# print(bj_11049())

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

def bj_7579():
    n,m=map(int,input().split())
    app_memory=[0]+list(map(int,input().split()))
    app_cost=[0]+list(map(int,input().split()))
    dp_map=[1000000000 for _ in range(m+1)]
    for app_index in range(1,n+1):
        tmp=[0 for _ in range(m+1)]
        for memory in range(0,m+1):
            if memory<=app_memory[app_index]:
                tmp[memory]=min(dp_map[memory],app_cost[app_index])
            else:
                tmp[memory]=min(dp_map[memory],dp_map[memory-app_memory[app_index]]+app_cost[app_index])
        dp_map=tmp

    return dp_map[-1]

# print(bj_7579())


def bj_11404():
    n=int(input())
    m=int(input())
    inf=100000000
    flood_map=[[inf for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        flood_map[i][i]=0
    for i in range(m):
        start,end,cost=map(int,input().split())
        if flood_map[start][end]>cost:
            flood_map[start][end]=cost
    # for flood in flood_map:
    #     print(flood[1:])

    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                flood_map[j][k]=min(flood_map[j][k],flood_map[j][i]+flood_map[i][k])
                # flood_map[i][j]=min(flood_map[i][j],flood_map[i][k]+flood_map[k][j])
    for i in range(1,n+1):
        for j in range(1,n+1):
            if flood_map[i][j]==inf:
                flood_map[i][j]=0
        
    return [maps[1: ]for maps in flood_map[1:]]

# result=bj_11404()
# for maps in result:
#     print(*maps)

def bj_1956():
    v,e=map(int,input().split())
    inf=100000000
    flood_map=[[inf for _ in range(v+1)] for _ in range(v+1)]
    for i in range(e):
        start,end,cost=map(int,input().split())
        flood_map[start][end]=cost
    for i in range(1,v+1):
        for j in range(1,v+1):
            for k in range(1,v+1):
                flood_map[j][k]=min(flood_map[j][k],flood_map[j][i]+flood_map[i][k])
    min_cost=inf
    for i in range(1,v+1):
        if flood_map[i][i]<min_cost:
            min_cost=flood_map[i][i]
    if min_cost==inf:
        return -1
    return min_cost

# print(bj_1956())

def bj_17404():
    h=int(input())
    rgb_list=[[0,0,0]]+[list(map(int,input().split())) for _ in range(h)]
    inf=1000000000
    ans=inf
    for i in range(3):
        dp_list=[[0,0,0]]+[[inf,inf,inf] for _ in range(h)]
        dp_list[1][i]=rgb_list[1][i]
        for j in range(2,h+1):
            dp_list[j][0]=rgb_list[j][0]+min(dp_list[j-1][1],dp_list[j-1][2])
            dp_list[j][1]=rgb_list[j][1]+min(dp_list[j-1][0],dp_list[j-1][2])
            dp_list[j][2]=rgb_list[j][2]+min(dp_list[j-1][0],dp_list[j-1][1])
        for j in range(3):
            if i!=j:
                ans=min(ans,dp_list[h][j])
    return ans

# print(bj_17404())

def bj_14002():
    n=int(input())
    num_list=list(map(int,input().split()))
    dp_list=[[num_list[i]] for i in range(n)]
    for i in range(n-2,-1,-1):
        max_count=0
        max_index=None
        for j in range(i+1,n):
            if num_list[i]<num_list[j] and len(dp_list[j])>max_count:
                max_count=len(dp_list[j])
                max_index=j
        if max_index:
            dp_list[i].extend([*dp_list[max_index]])  
    return (max(dp_list,key=lambda x:len(x)))
# result=bj_14002()
# print(len(result))
# print(" ".join(str(num) for num in result))

def bj_9252():
    string1=" "+input()
    string2=" "+input()
    dp_list=[[0 for _ in range(len(string1))] for _ in range(len(string2))]
    for i in range(1,len(string2)):
        for j in range(1,len(string1)):
            if string1[j]==string2[i]:
                dp_list[i][j]=dp_list[i-1][j-1]+1
            else:
                dp_list[i][j]=max(dp_list[i][j-1],dp_list[i-1][j])
    result=[]
    x=len(string1)-1
    y=len(string2)-1
    while x>0 and y>0:
        if dp_list[y][x-1]==dp_list[y][x]:
            x-=1
        elif dp_list[y-1][x]==dp_list[y][x]:
            y-=1
        else:
            result.append(string1[x])
            x-=1
            y-=1
    return "".join(reversed(result))

# result=bj_9252()
# print(len(result))
# if result:
#     print(result)

def bj_1019():
    n=int(input())
    units=n%10
    tens=n//10
    first_list=[tens+1 for _ in range(10)]
    tens_list=[0 for _ in range(10)]
    for i in range(10):
        tens_list[i]+=tens//10*100
        if tens%10>=i:
            tens_list[i]+=(tens%10)*10
    result=[first_list[i]+tens_list[i] for i in range(10)]
    for i in range(9,units,-1):
        result[i]-=1
        result[tens%10]-=1
    result[0]-=1
    print(result)
    
            
    
    
    return 1

# print(bj_1019())


def bj_1916():
    n=int(input())
    cost_list=[[] for _ in range(n+1)]
    m=int(input())
    for i in range(m):
        start,end,cost=map(int,input().split())
        cost_list[start].append((end,cost))
    start,end=map(int,input().split())

    min_dis=[10000000000 for i in range(n+1)]
    min_dis[start]=0
    to_do_list=[]
    heappush(to_do_list,(0,start))
    while len(to_do_list)>=1:
        print(to_do_list)
        print("min_dis",min_dis)
        dis,do=heappop(to_do_list)
        if min_dis[do]<dis:
            continue
        for to_do,to_do_dis in cost_list[do]:
            if dis+to_do_dis<min_dis[to_do]:
                min_dis[to_do]=dis+to_do_dis
                heappush(to_do_list,(min_dis[to_do],to_do))
    return min_dis[end]
# print(bj_1916())

def bj_11779():
    n=int(input())
    cost_list=[[] for _ in range(n+1)]
    m=int(input())
    for i in range(m):
        start,end,cost=map(int,input().split())
        cost_list[start].append((end,cost))
    start,end=map(int,input().split())

    min_dis=[10000000000 for i in range(n+1)]
    min_dis[start]=0
    to_do_list=[]
    path_list=[0 for _ in range(n+1)]
    heappush(to_do_list,(0,start))
    while len(to_do_list)>=1:
        dis,do=heappop(to_do_list)

        if min_dis[do]<dis:
            continue

        for to_do,to_do_dis in cost_list[do]:
            if dis+to_do_dis<min_dis[to_do]:
                min_dis[to_do]=dis+to_do_dis
                path_list[to_do]=do
                heappush(to_do_list,(min_dis[to_do],to_do))
    result=[]
    back_track=end
    while path_list[back_track]!=0:
        result.append(back_track)
        back_track=path_list[back_track]
    result.append(start)
    result=list(reversed(result))
    return (result,min_dis[end])
# path_list,min_dis=bj_11779()
# print(min_dis)
# print(len(path_list))
# print(" ".join([str(city) for city in path_list]))

def bj_1976():
    n=int(input())
    m=int(input())
    inf=10000000000000
    dis_list=[[inf for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        load_list=list(map(int,input().split()))
        for j in range(n):
            if load_list[j]==1:
                dis_list[i+1][j+1]=1
                dis_list[j+1][i+1]=1
    for i in range(n+1):
        dis_list[i][i]=1
    travel_list=list(map(int,input().split()))
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                dis_list[j][k]=min(dis_list[j][k],dis_list[j][i]+dis_list[i][k])
    for i in range(len(travel_list)-1):
        pre_city=travel_list[i]
        next_city=travel_list[i+1]
        if dis_list[pre_city][next_city]>=inf:
            return "NO"
    return "YES"

# print(bj_1976())
def find_par(x,list):
    if x==list[x]:
        return x
    list[x]=find_par(list[x],list)
    return list[x]

def bj_10775():
    G=int(input())
    Gate_list=[i for i in range(G+1)]
    P=int(input())
    # arrive_list=[int(input()) for _ in range(P)]
    arrive_list=[i for i in range(2000,1,-1)]+[1500]
    count=0
    for arrive_num in arrive_list:
        print(arrive_num)
        max_gate=find_par(arrive_num,Gate_list)
        if max_gate==0:
            return count
        Gate_list[max_gate]=find_par(max_gate-1,Gate_list)
        print(Gate_list)
        count+=1
    return count

# print(bj_10775())

def find_par(x,list):
    if x==list[x]:
        return x
    list[x]=find_par(list[x],list)
    return list[x]

def bj_1197():
    v,e=map(int,input().split())
    edges=[list(map(int,input().split())) for _ in range(e)]
    sorted_edge=sorted(edges,key=lambda x:x[2])
    parent=[i for i in range(v+1)]
    min_cost=0
    for start,end,cost in sorted_edge:
        start_parent=find_par(start,parent)
        right_parent=find_par(end,parent)
        if start_parent!=right_parent:
            min_cost+=cost
            if start_parent<right_parent:
                parent[right_parent]=start_parent
            else:
                parent[start_parent]=right_parent

    return min_cost

# print(bj_1197())

def find_par(x,list):
    if x==list[x]:
        return x
    list[x]=find_par(list[x],list)
    return list[x]

def bj_4386():
    n=int(input())
    x_y=[list(map(float,input().split())) for _ in range(n)]
    cost_list=[]
    for i in range(n):
        for j in range(n):
            dis=math.sqrt((x_y[i][0]-x_y[j][0])**2+(x_y[i][1]-x_y[j][1])**2)
            cost_list.append((i,j,dis))
    sorted_cost=sorted(cost_list,key=lambda x:x[2])
    par_list=[i for i in range(n)]
    min_cost=0
    for start,end,cost in sorted_cost:
        start_par=find_par(start,par_list)
        end_par=find_par(end,par_list)
        if start_par!=end_par:
            min_cost+=cost
            if start_par<end_par:
                par_list[end_par]=start_par
            else:
                par_list[start_par]=end_par
    return round(min_cost,3)

# print(bj_4386())


def bj_10282():
    test=int(input())
    result=[]
    for _ in range(test):
        n,d,c=map(int,input().split())
        com=[[] for _ in range(n+1)]
        for i in range(d):
            start,end,cost=map(int,input().split())
            com[end].append((start,cost))
        inf=10000000000
        min_cost=[inf for i in range(n+1)]
        min_cost[c]=0
        to_do_list=[]
        to_do_list.append((0,c))
        while len(to_do_list)>=1:
            cost,do=heappop(to_do_list)
            if min_cost[do]<cost:
                continue
            for to_do,to_do_cost in com[do]:
                if cost+to_do_cost<min_cost[to_do]:
                    min_cost[to_do]=cost+to_do_cost
                    heappush(to_do_list,(cost+to_do_cost,to_do))
        count=0
        max=0
        for i in range(1,n+1):   
            if min_cost[i]<inf:
                count+=1
                if max<=min_cost[i]:
                    max=min_cost[i]
        result.append((count,max))
    return result
# result=bj_10282()
# for count,min_cost in result:
#     print(count,min_cost)

# def bj_15681():
#     n,r,q=map(int,input().split())
#     graph=[[] for _ in range(n+1)]
#     for _ in range(n-1):
#         start,end=map(int,input().split())
#         graph[start].append(end)
#         graph[end].append(start)
#     q_list=[int(input()) for _ in range(q)]
    
#     visited=[False for _ in range(n+1)]
#     to_do_list=deque()
#     visited[r]=True
#     to_do_list.append(r)
#     order_list=[r]
#     direct_graph=[[] for _ in range(n+1)]
#     while len(to_do_list)>=1:
#         do=to_do_list.popleft()
#         for to_do in graph[do]:
#             if visited[to_do]==False:
#                 to_do_list.append(to_do)
#                 direct_graph[do].append(to_do)
#                 order_list.append(to_do)
#                 visited[to_do]=True
#     order_list=list(reversed(order_list))
#     dp_list=[0 for _ in range(n+1)]
#     for node in order_list:
#         if direct_graph[node]==[]:
#             dp_list[node]=1
#         else:
#             count=0
#             for child_node in direct_graph[node]:
#                 count+=dp_list[child_node]
#             dp_list[node]=count+1
#     result=[]
#     for num in q_list:
#         result.append(dp_list[num])
#     return result

# result=bj_15681()
# for num in result:
#     print(num)
    

def count_subtree(do,graph,visited,dp_list):
    visited[do]=True
    if graph[do]==[]:
        dp_list[do]=1
        return 1
    count=0
    for to_do in graph[do]:
        if visited[to_do]==False:
            count+=count_subtree(to_do,graph,visited,dp_list)
    dp_list[do]=count+1
    return count+1

def bj_15681():
    sys.setrecursionlimit(10**5)
    n,r,q=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(n-1):
        start,end=map(int,input().split())
        graph[start].append(end)
        graph[end].append(start)
    q_list=[int(input()) for _ in range(q)]
    visited=[False for _ in range(n+1)]
    dp_list=[0 for _ in range(n+1)]
    count_subtree(r,graph,visited,dp_list)
    result=[dp_list[num] for num in q_list]
    return result
# result=bj_15681()
# for num in result:
#     print(num)

def dfs(node,graph,dp,visited):
    visited[node]=True
    for next_node in graph[node]:
        if visited[next_node]==False:
            dfs(next_node,graph,dp,visited)
            #node가 우수마을이 아닌 경우 해당 마을 아래포함 최대 우수마을 주민 수
            #주변 노드는 우수마을 또는 아닌 우수마을이 아닌 경우 최대 아래포함 우수마을 주민 수
            dp[node][0]+=max(dp[next_node])
            #node가 우수마을인 경우 해당 마을 아래포함 최대 우수마을 주민 수
            #주변 노드는 우수마을이 아닌 경우 아래포함 최대 우수마을 주민 수를 합
            dp[node][1]+=dp[next_node][0]
    

def bj_1949():
    n=int(input())
    sys.setrecursionlimit(10**5)
    cost_list=[0]+list(map(int,input().split()))
    graph_list=[[] for _ in range(n+1)]
    for _ in range(n-1):
        start,end=map(int,input().split())
        graph_list[start].append(end)
        graph_list[end].append(start)
    dp_list=[[0,cost_list[i]] for i in range(n+1)]
    visited=[False for _ in range(n+1)]
    dfs(1,graph_list,dp_list,visited)
    print(dp_list)
    return max(dp_list[1])
# print(bj_1949())



def dfs(node,graph,dp,visited):
    visited[node]=True
    for next_node in graph[node]:
        if visited[next_node]==False:
            dfs(next_node,graph,dp,visited)
            #node가 우수마을이 아닌 경우 해당 마을 아래포함 최대 우수마을 주민 수
            #주변 노드는 우수마을 또는 아닌 우수마을이 아닌 경우 최대 아래포함 우수마을 주민 수
            dp[node][0]+=max(dp[next_node])
            #node가 우수마을인 경우 해당 마을 아래포함 최대 우수마을 주민 수
            #주변 노드는 우수마을이 아닌 경우 아래포함 최대 우수마을 주민 수를 합
            dp[node][1]+=dp[next_node][0]

def track(node,graph,dp,visited,path,picked):
    visited[node]=True
    for next_node in graph[node]:
        if visited[next_node]==False:
            if picked:
                path.append((next_node,0))
                track(next_node,graph,dp,visited,path,False)
            else:
                if dp[next_node][0]>dp[next_node][1]:
                    path.append((next_node,0))
                    track(next_node,graph,dp,visited,path,False)
                else:
                    path.append((next_node,1))
                    track(next_node,graph,dp,visited,path,True)
            
def bj_2213():
    n=int(input())
    sys.setrecursionlimit(10**5)
    cost_list=[0]+list(map(int,input().split()))
    graph_list=[[] for _ in range(n+1)]
    for _ in range(n-1):
        start,end=map(int,input().split())
        graph_list[start].append(end)
        graph_list[end].append(start)
    dp_list=[[0,cost_list[i]] for i in range(n+1)]
    visited=[False for _ in range(n+1)]
    path=[[],[]]
    dfs(1,graph_list,dp_list,visited)
    visited=[False for _ in range(n+1)]
    path=[]
    if dp_list[1][0]>dp_list[1][1]:
        path.append((1,0))
        track(1,graph_list,dp_list,visited,path,False)
    else:
        path.append((1,1))
        track(1,graph_list,dp_list,visited,path,True)
    return (max(dp_list[1]),sorted([node for node,picked in path if picked==1]))
# result=bj_2213()
# print(result[0])
# print(" ".join(list(map(str,result[1]))))

def bj_1701():
    strings=input()  
    max_lps=0

    for i in range(len(strings)):
        pat=strings[i:]
        leng=0
        j=1
        lps=[0 for _ in range(len(pat))]
        while j<len(pat):
            if pat[j]==pat[leng]:
                leng+=1
                lps[j]=leng
                j+=1
            else:
                if leng!=0:
                    leng=lps[leng-1]
                else:
                    lps[j]=0
                    j+=1
        max_lps=max(max(lps),max_lps)
    return max_lps
# print(bj_1701())

class Node:
    def __init__(self,key=None,data=None):
        self.key=key
        self.data=data
        self.children={}

class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,fruits):
        current_node=self.root
        for fruit in fruits:
            if fruit not in current_node.children:
                current_node.children[fruit]=Node(fruit)
            # print(current_node.children)
            current_node=current_node.children[fruit]
        current_node.data=fruits
    
    # def dfs(self,node,depth):
    #     for key in sorted(node.children.keys()):
    #         print("-"*depth*2+key)
    #         self.dfs(node.children[key],depth+1)
            
    def dfs(self,node,depth):
        to_do_list=[(node,depth)]
        while len(to_do_list)>=1:
            node,depth=to_do_list.pop()
            if node.key:
                print("-"*(depth-1)*2+node.key)
            for key in sorted(node.children.keys(),reverse=True):
                to_do_list.append((node.children[key],depth+1))
            

         

def bj_14725():
    n=int(input ())
    trie=Trie()
    for i in range(n):
        fruits=list(input().split())[1:]
        trie.insert(fruits)

    return trie
# result=bj_14725()
# result.dfs(result.root,0)

