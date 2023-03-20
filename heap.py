from heapq import heapify,heappush,heappop
import math
def heap_42626(scoville, K):
    heapify(scoville)
    count=0

    while len(scoville)>=2:
        sco1=heappop(scoville)
        if sco1>=K:
            return count
        else:
            count+=1
            sco2=heappop(scoville)
            sco3=sco1+2*sco2
            heappush(scoville,sco3)
    
    if scoville[0]>=K:
        return count
    
    return -1
        
    
# scoville=[5,5,5,5,5,5]
# K=4
# print(heap_42626(scoville,K))

def heap_42627(jobs):
    heapify(jobs)
    result=[]
    current_time=0
    to_do_jobs=[]
    while (len(jobs)>=1 or len(to_do_jobs)>=1):
        while(len(jobs)>=1 and jobs[0][0]<=current_time):
            heappush(to_do_jobs,list(reversed(heappop(jobs))))
        if len(to_do_jobs)>=1:
            current_job=heappop(to_do_jobs)
            result.append(current_time-current_job[1]+current_job[0])
            current_time+=current_job[0]
        else:
            current_job=heappop(jobs)
            result.append(current_job[1])
            current_time=current_job[0]+current_job[1]
        # print(current_job)
        # print(current_time)
    # print(result)

    return math.trunc(sum(result)/len(result))

# jobs=[[0, 5], [2, 10], [10000, 2]]
# print(heap_42627(jobs))

def heap_42628(operations):
    nums_min_heap=[]
    nums_max_heap=[]
    hash_map={}
    for order in operations:
        order=order.split(' ')
        alpha=order[0]
        num=int(order[1])
        if alpha=='I':
            heappush(nums_min_heap,num)
            heappush(nums_max_heap,(-num,num))
            if num not in hash_map:
                hash_map[num]=1
            else:
                hash_map[num]+=1
        if alpha=='D' and num==1:
            while len(nums_max_heap)>=1 and hash_map[nums_max_heap[0][1]]<1:
                heappop(nums_max_heap)
            if len(nums_max_heap)>=1:
                max_num=heappop(nums_max_heap)    
                hash_map[max_num[1]]-=1       
            
        if alpha=='D' and num==-1:
            while len(nums_min_heap)>=1 and hash_map[nums_min_heap[0]]<1:
                heappop(nums_min_heap)
            if len(nums_min_heap)>=1:
                min_num=heappop(nums_min_heap)
                hash_map[min_num]-=1
    
        # print(alpha,num)
        # print('hash',hash_map)
        # print('nums',nums_min_heap,nums_max_heap)
    result=[]
    for [num,count] in hash_map.items():
        if count>=1:
            result.extend([num]*count)
    result=sorted(result,reverse=True)
    # print(result)
    if len(result)<1:
        return [0,0]
    elif len(result)==1:
        return [result[0],result[0]]
    else:
        return [result[0],result[-1]]
operations=["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(heap_42628(operations))
