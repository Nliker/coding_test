from collections import deque

v,e=map(int,input().split())

#각 노드들로 들어오는 노드의 갯수 초기화
indegree=[0 for _ in range(v+1)]
#그래프 초기화
graph=[[] for _ in range(v+1)]

for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    #받는 노드의 갯수 추가
    indegree[b]+=1

result=[]
to_do_list=deque([(i,0) for i in range(1,v+1) if indegree[i]==0])
while len(to_do_list)>0:
    do,depth=to_do_list.popleft()
    #순서 추가
    result.append((do,depth))
    #인접노드들 방문
    for to_do in graph[do]:
        #인접노드 입장에서 do를 이미 방문했으므로 들어오는 노드 갯수 감소
        indegree[to_do]-=1
        #들어오는 노드 갯수가 모두 완료 되었을때 해당 노드 추가
        if indegree[to_do]==0:
            to_do_list.append((to_do,depth+1))

print(result)

# e=int(input())

# indegree={}
# graph={}

# for i in range(e):
#     a,b=input().split()
#     if a not in graph:
#         graph[a]=[]
#     if b not in graph:
#         graph[b]=[]
#     graph[a].append(b)
    
#     if a not in indegree:
#         indegree[a]=0
#     if b not in indegree:
#         indegree[b]=0
#     indegree[b]+=1
    
# result=[]
# to_do_list=deque()
# for key,value in indegree.items():
#     if value==0:
#         to_do_list.append((key,0))
        
# while len(to_do_list)>0:
#     do,depth=to_do_list.popleft()
#     result.append((do,depth))
#     for to_do in graph[do]:
#         indegree[to_do]-=1
#         if indegree[to_do]==0:
#             to_do_list.append((to_do,depth+1))
# for i in range(depth+1):
#     print("depth==========",i,"==================")
#     for subjects,depth in result:
#         if depth==i:
#             print(subjects)