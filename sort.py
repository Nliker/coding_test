from functools import cmp_to_key,reduce
def sort_42748(array, commands):
    result=[]
    for [start,end,k] in commands:
        sorted_list=sorted(array[start-1:end])
        result.append(sorted_list[k-1])
    return result

# array=[1, 5, 2, 6, 3, 7, 4]	
# commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(sort_42748(array, commands))

def sort_42746(numbers):
    numbers.sort(key=cmp_to_key(lambda a,b: -1 if int(str(a)+str(b))>=int(str(b)+str(a)) else 1))
    return "0" if numbers[0]==0 else reduce(lambda acc,value:acc+str(value),numbers,"")

# numbers=[3, 30, 34, 5, 9]	
# print(sort_42746(numbers))

def sort_42747(citations):
    # hash_citations={}
    # for i in citations:
    #     if i not in hash_citations:
    #         hash_citations[i]=1
    #     else:
    #         hash_citations[i]+=1
    # sorted_citations=sorted(hash_citations.items(),key=lambda x:x[0],reverse=True)
    # count=0
    # h_index=0
    # for citation in sorted_citations:
    #     count+=citation[1]
    #     temp=0
    #     if citation[0]<=count:
    #         temp=citation[0]
    #     else:
    #         temp=count
    #     if h_index<=temp:
    #         h_index=temp
    # return h_index
    citations.sort(reverse=True)
    for i,citation in enumerate(citations):
        if citation<i+1:
            return i
    return len(citations)
citations=[0]
print(sort_42747(citations))
# 5,5,5,5,1
# 10,2,2
# 1,1,1,0
# 5,5,4,4,4
# 5,5,5,5,1
# 5,5,4,
