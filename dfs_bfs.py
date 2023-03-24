from collections import deque
from heapq import heapify,heappush,heappop
# graph = [
#     [],
#     [2, 3, 4],
#     [1, 5, 6],
#     [1],
#     [1, 7],
#     [2],
#     [2, 8],
#     [4],
#     [ 6]
# ]

# visited=[False]*len(graph)
# print(visited)

def dfs_recur(graph,node,visited):
    print(node)
    visited[node]=True
    for node in graph[node]:
        if visited[node]==False:
            dfs_recur(graph,node,visited)
    
    return 1

# print(dfs_recur(graph,1,visited),visited)

def dfs_stack(graph,node,visited):
    list=deque()
    list.append(node)
    while len(list)>=1:
        print(list)
        node=list.pop()
        print(node)
        visited[node]=True
        for node in graph[node]:
            if visited[node]==False:
                list.append(node)
    return 1

# print(dfs_stack(graph,1,visited),visited)

def bfs_stack(graph,node,visited):
    list=deque()
    list.append(node)
    while len(list)>=1:
        node=list.popleft()
        print(node)
        visited[node]=True
        for node in graph[node]:
            if visited[node]==False:
                list.append(node)

    return 1
# print(bfs_stack(graph,1,visited),visited)

def dfs_target(numbers,target,depth):
    count=0
    if depth==len(numbers):
        if target==0:
            return 1
        return 0
    count+=dfs_target(numbers,target+numbers[depth],depth+1)
    count+=dfs_target(numbers,target-numbers[depth],depth+1)
    return count

def dfs_bfs_43165(numbers, target):
    result=dfs_target(numbers,target,0)
    return result

# numbers=[4, 1, 2, 1]
# target=	4
# print(dfs_bfs_43165(numbers,target))


def dfs_bfs_1844(maps):
    visited=[[False]*len(maps[0]) for i in range(len(maps))]
    list=deque()
    distance=1
    list.append((0,0,distance)) 
    visited[0][0]=True
    x_offset=[-1,1,0,0]
    y_offset=[0,0,-1,1]
    while len(list)>=1:
        x,y,d=list.popleft()
        if (x,y)==(len(maps)-1,len(maps[0])-1):
            return d
        indexes=[(x+x_offset[i],y+y_offset[i]) for i in range(4)]
        for x,y in indexes:
            if x>=0 and x<=len(maps)-1 and y>=0 and y<=len(maps[0])-1 and maps[x][y]==1 and visited[x][y]==False:
                list.append((x,y,d+1))     
                visited[x][y]=True
    return -1
# maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# print(dfs_bfs_1844(maps))

def dfs_bfs_test(maps):
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue.append([0,0])
    while queue:
        [a, b]=queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] == 1:
                queue.append([x, y])
                maps[x][y] = maps[a][b] + 1
    des_distance=maps[len(maps)-1][len(maps[0])-1]
    return -1 if des_distance==1 else des_distance 

maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(dfs_bfs_test(maps))

def dfs_bfs_area_test(maps):
    visited=[[False]*len(maps[0]) for i in range(len(maps))]
    count_list=[]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visited[i][j]==False and maps[i][j]==1:
                list=deque()
                list.append((0,0)) 
                visited[i][j]=True
                x_offset=[-1,1,0,0]
                y_offset=[0,0,-1,1]
                count=0
                while len(list)>=1:
                    count+=1
                    x,y=list.pop()
                    indexes=[(x+x_offset[i],y+y_offset[i]) for i in range(4)]
                    for x,y in indexes:
                        if x>=0 and x<=len(maps)-1 and y>=0 and y<=len(maps[0])-1 and maps[x][y]==1 and visited[x][y]==False:
                            list.append((x,y))     
                            visited[x][y]=True                
    for i in visited:
        print(i)
    return count_list
# maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# print(dfs_bfs_test(maps))
            
def dfs_bfs_43162(n,computers):
    visited=[False for i in range(n)]
    net_count=0
    def dfs_43162(computers,node,visited):
        visited[node]=True
        for computer,connect in enumerate(computers[node]):
            if node!=computer and visited[computer]==False and connect==1:
                dfs_43162(computers,computer,visited)
    for computer in range(n):
        if visited[computer]==False:
            dfs_43162(computers,computer,visited)
            net_count+=1
    
    return net_count

# n=3	
# computers=	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

# print(dfs_bfs_43162(n,computers))


def dfs_bfs_43163(begin,target,words):
    words.append(begin)
    list=[[] for i in range(len(words))]
    for comp_index,comp_word in enumerate(words):
        for index,word in enumerate(words):
            if comp_index!=index:
                count=0
                for i,ch in enumerate(word):
                    if comp_word[i]!=ch:
                        count+=1
                if count==1:
                    list[comp_index].append(index)
    visited=[False for i in range(len(words))]
    to_do_list=deque()
    start_do=len(words)-1
    to_do_list.append((start_do,0))
    visited[start_do]=True
    while len(to_do_list):   
        do,r=to_do_list.popleft()
        if words[do]==target:
            return r
        for to_do in list[do]:
            if visited[to_do]==False:
                visited[to_do]=True
                to_do_list.append((to_do,r+1))  
    return 0
# begin="hit"
# target="cog"
# words=["hot", "dot", "dog", "lot", "log", "cog"]	

# print(dfs_bfs_43163(begin,target,words))


def dfs_dep_to_des(dep,des,hash_map):
    if dep==des:
        return True
    if dep not in hash_map:
        return False
    for next_dep in hash_map[dep]:
        result=dfs_dep_to_des(next_dep[1],des,hash_map)
        
    return result
def dfs_bfs_43164(tickets):
    hash_map={}
    for [dep,des] in tickets:
        if dep not in hash_map:
            hash_map[dep]=[([-ord(character) for character in des],des)]
        else:
            heappush(hash_map[dep],([-ord(character) for character in des],des))
    to_do_list=deque()
    to_do_list.append("ICN")
    travel_list=[]
    while len(to_do_list)>=1:
        do=to_do_list.pop()
        travel_list.append(do)
        if do not in hash_map:
            break
        can_return_list=[]
        cannot_return_port=None
        for i in range(len(hash_map[do])):
            temp_do=hash_map[do][i]
            if  dfs_dep_to_des(temp_do[1],do,hash_map)==False:
                cannot_return_port=temp_do[1]
            else:
                heappush(can_return_list,temp_do)

        hash_map[do]=can_return_list
        if cannot_return_port!=None:
            to_do_list.append(cannot_return_port)
        for i in range(len((can_return_list))):
            next_do=heappop(can_return_list)
            to_do_list.append(next_do[1])
            
        # for i in range(len(hash_map[do])):
        #     next_do=heappop(hash_map[do])
        #     print('리컬 전',next_do[1],do)
        #     print(dfs_dep_to_des(next_do[1],do,hash_map))
        #     if len(hash_map[do])>1 and dfs_dep_to_des(next_do[1],do,hash_map)==True:
        #         temp_next_do=heappop(hash_map[do])
        #         heappush(hash_map[do],next_do)
        #         next_do=temp_next_do     
        #     to_do_list.append(next_do[1])     
        print("to_do_list",to_do_list)      
                
    return travel_list

# tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# print(dfs_bfs_43164(tickets))

# list=[[1,2],
#       [3],
#       [4,5],
#       [6],
#       [],
#       [7,8],
#       [9],
#       [],
#       [],
#       [10],
#       []]

# def dfs_depth_cur(node,list):
#     if list[node]==[]:
#         return 0
#     max=0
#     for node in list[node]:
#         depth=dfs_depth_cur(node,list)
#         if max<depth:
#             max=depth
#     return max+1
# print("최대깊이는")
# print(dfs_depth_cur(0,list))
# print("최대깊이는")

# def print_bfs(list):
#     to_do=deque()
#     to_do.append(0)
    
#     while len(to_do)>=1:
#         for i in range(len(to_do)):
#             node=to_do.popleft()
#             print(node,end=" ")
#             for next_node in list[node]:
#                 to_do.append(next_node)
#         print(" ")
#     return "good"
# print(print_bfs(list))

def dj(graph,node):
    min_dis=[10000 for i in range(len(graph))]
    min_dis[node]=0
    to_do_list=[]
    heappush(to_do_list,(0,node))
    while len(to_do_list)>=1:
        dis,do=heappop(to_do_list)
        if min_dis[do]<dis:
            continue
        for to_do,to_do_dis in graph[do]:
            if dis+to_do_dis<min_dis[to_do]:
                min_dis[to_do]=dis+to_do_dis
                heappush(to_do_list,(min_dis[to_do],to_do))
                
    return min_dis
graph1=[
    [(2,1),(3,3),(4,3)],
    [(6,2),(4,2)],
    [(5,5)],
    [(4,3)],
    [(5,2),(6,3)],
    [(6,1)],
    []
]
graph2=[
    [(1,3),(2,5),(3,1)],
    [(0,3),(2,4),(3,3)],
    [(0,5),(1,4),(3,2)],
    [(0,1),(1,3),(2,2)]
]
graph3=[
    [(1,3)],
    [(0,4)]
]
for i in range(len(graph1)):  
    print(dj(graph1,i))
print("=============")
def flood(graph):
    inf=100000000
    n=len(graph)
    min_dis=[[inf for i in range(n)]for j in range(n)]
    for i in range(n):
        min_dis[i][i]=0
    for do,to_do_list in enumerate(graph):
        for to_do,dis in to_do_list:
            min_dis[do][to_do]=dis
            min_dis[to_do][do]=dis
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                min_dis[j][k]=min(min_dis[j][k],min_dis[j][i]+min_dis[i][k])
    
    for i in min_dis:
        print(i)
                
    
    return 1

print(flood(graph1))


