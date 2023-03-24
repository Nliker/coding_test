from collections import deque
def greedy_42862(n,lost,reserve):
    hash_reserve={}
    for i in reserve:
        if i in lost:
            hash_reserve[i]=1
        else:
            hash_reserve[i]=2
    lost_count=0
    for i in sorted(lost):
        if i in hash_reserve and hash_reserve[i]>=1:
            continue
        if i-1 in hash_reserve and hash_reserve[i-1]==2:
            hash_reserve[i-1]=1
        elif i+1 in hash_reserve and hash_reserve[i+1]==2:
            hash_reserve[i+1]=1
        else:
            lost_count+=1
    return n-lost_count
    
# n=5
# lost=[4,2]
# reserve=[3,5]	
# print(greedy_42862(n,lost,reserve))

def greedy_42860(name):
    sub_name=["A"]*len(name)
    count=0
    index=0
    while "".join(sub_name)!=name:
        alpha_count=min(ord(name[index])-ord("A"),ord("Z")-ord(name[index])+1)
        sub_name[index]=name[index]
        count+=alpha_count
        left_distance=1

        while sub_name[(index-left_distance)%len(name)]==name[(index-left_distance)%len(name)]:
            left_distance+=1
            if left_distance>=len(sub_name):
                return count
        right_distance=1

        while sub_name[(index+right_distance)%len(name)]==name[(index+right_distance)%len(name)]:
            right_distance+=1
            if right_distance>=len(sub_name):
                return count
        if left_distance<right_distance:
            count+=left_distance
            index=(index-left_distance)%len(name)
        else:
            count+=right_distance
            index=(index+right_distance)%len(name)
    return count
# name="ABABAAAAABA"
# print(greedy_42860(name))

def greedy_42883(number,k):
    result=[number[0]]
    for num in number[1:]:
        while result and k!=0 and result[-1]<num:
            k-=1
            result.pop()
        result.append(num)
    return "".join(result[:len(result)-k])

# number="4177252841"	
# k=4
# print(greedy_42883(number,k))

def greedy_42885(people,limit):
    count=0
    people_deque=deque(sorted(people))
    while len(people_deque)>=1:
        light_people=people_deque.popleft()
        while len(people_deque)>=1 and light_people+people_deque[-1]>limit:
            people_deque.pop()
            count+=1
        if len(people_deque)>=1:
            people_deque.pop()
        count+=1
    return count
# people=[1,2,3,4,5,6,7,8,9,10] 
# limit=10
# print(greedy_42885(people,limit))

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def greedy_42861(n, costs):
    parent=[i for i in range(n)]
    edges=sorted(costs,key=lambda x:x[2])
    min_cost=0
    for edge in edges:
        left_ele_parent=find_parent(parent,edge[0])
        right_ele_parent=find_parent(parent,edge[1])
        if left_ele_parent!=right_ele_parent:
            min_cost+=edge[2]
            if left_ele_parent<right_ele_parent:
                parent[right_ele_parent]=left_ele_parent
            else:
                parent[left_ele_parent]=right_ele_parent
    return min_cost
n=4
costs=[[2,3,8],[0,1,1],[0,2,2],[1,2,5],[1,3,1]]	
print(greedy_42861(n,costs))

