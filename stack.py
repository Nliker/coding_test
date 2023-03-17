from collections import deque

def stack_12906(arr):
    stack=deque()
    for char in arr:
        if len(stack)==0:
            stack.append(char)
        elif len(stack)>=1 and stack[-1]!=char:
            stack.append(char)

    return list(stack)
            
# arr=[4,4,4,4,2,2,2,1,1,1,4,4,3,3]
# print(stack_12906(arr))

import math

def stack_42586(progresses, speeds):
    queue=deque(progresses)
    speeds=deque(speeds)
    result=[]
    while len(queue)>=1:
        days=math.ceil((100-queue[0])/speeds[0])
        count=0
        while len(queue)>=1 and queue[0]+days*speeds[0]>=100:
            queue.popleft()
            speeds.popleft()
            count+=1
        result.append(count)
    return result

# progresses=[95, 90, 99, 99, 80, 99]
# speeds=[1,1,1,1,1,1]

# print(stack_42586(progresses,speeds))

def stack_12909(s):
    stack=deque()
    for char in s:
        if len(stack)==0:
            if char ==")":
                return False
            stack.append(char)
        elif char=='(':
            stack.append(char)
        else:
            stack.pop()
            
    return (True if len(stack)==0 else False)

# s="(())()"
# print(stack_12909(s))

def stack_42587(priorities, location):
    queue=deque()
    for i,priority in enumerate(priorities):
        queue.append((priority,i))
    result=[]
    while len(queue)>=1:
        temp=queue.popleft()
        bigger_exists=False
        for i in queue:
            if i[0]>temp[0]:
                bigger_exists=True
                break
        if bigger_exists:
            queue.append(temp)
        else:
            result.append(temp[1])
    for i,v in enumerate(result):
        if v==location:
            return i+1


# prioritie=[2, 1, 3, 2]	
# location=2

# print(stack_42587(prioritie, location))

def stack_42583(bridge_length, weight, truck_weights):
    count=0
    bridge_queue=deque([0]*bridge_length)
    bridge_weight=0
    truck_queue=deque(truck_weights)
    
    while(len(bridge_queue)>=1):
        count+=1
        bridge_weight-=bridge_queue.popleft()
        if len(truck_queue)>=1:
            if truck_queue[0]+bridge_weight<=weight:
                load_truck=truck_queue.popleft()
                bridge_weight+=load_truck
                bridge_queue.append(load_truck)
            else:
                bridge_queue.append(0)
    return count
# bridge_length=2
# weight=10
# truck_weights=	[7,4,5,6]

# print(stack_42583(bridge_length, weight, truck_weights))


def stack_42584(prices):
    prices_queue=deque(prices)
    result=[]
    while (len(prices_queue)>=1):
        count=0
        temp=prices_queue.popleft()
    
        for i in prices_queue:
            count+=1
            if temp>i:
                break
        result.append(count)
    
    return result
        
# prices=[4,2,4,2,3,1,2]
# print(stack_42584(prices))