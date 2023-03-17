def hash_1845(nums):
    h_m={}
    
    for num in nums:
        if num in h_m:
            h_m[num]+=1
        else:
            h_m[num]=1

    return int(len(h_m) if len(h_m)<len(nums)/2 else len(nums)/2)
   
# nums=[3,3,3,2,2,2]	
# print(hash_1845(nums))


def hash_42576(participant, completion):
    h_p={}
    
    for par in participant:
        if par in h_p:
            h_p[par]+=1
        else:
            h_p[par]=1
    
    for com in completion:
        h_p[com]-=1

    return next(name for name,v in h_p.items() if v==1)
    
# participant=["mislav", "stanko", "mislav", "ana"]
# completion=["stanko", "ana", "mislav"]
# print(hash_42576(participant,completion))

def hash_42577(phone_book):
    p_h={}
    for phone_num in phone_book:
        p_h[phone_num]=1
            
    for phone_num in phone_book:
        for i in range(len(phone_num)):
            pre_fix=phone_num[:i]
            if pre_fix in p_h:
                return False

    return True


# phone_book=["12","123","1235","567","88"]
# print(hash_42577(phone_book))

def hash_42578(clothes):
    c_h={}
    
    for [name,type] in clothes:
        if type in c_h:
            c_h[type]+=1
        else:
            c_h[type]=1
    values=c_h.values()
    count=1
    for i in values:
        count*=(i+1)
    return count-1
# clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],["green_turban", "headgea"], ["green_turban", "headgear"],["green_turban", "headgear"],["green_turban", "headgear"],["green_turban", "headgear"]]
# print(hash_42578(clothes))

def hash_42579(genres,plays):
    g_h={}
    g_h_i={}
    for i,genre in enumerate(genres):
        if genre in g_h:
            g_h[genre]+=plays[i]
            g_h_i[genre].append(i)
        else:
            g_h[genre]=plays[i]
            g_h_i[genre]=[i]
        
    sorted_g_h=sorted(g_h.items(),key=lambda item:-item[1])
    result=[]
    for (genre,v) in sorted_g_h:
        sorted_g_i=sorted(g_h_i[genre],key=lambda index:(-plays[index],index))
        result.extend(sorted_g_i[:2])
    
    return result
        
genres=["pop","pop","classic","classic","classic","classic","elec"]	
plays=[450,450,500, 500, 150, 800,550]	

print(hash_42579(genres,plays))
