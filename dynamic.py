from itertools import combinations

def dynamic_43105(triangle):
    pre_sum_list=[triangle[0][0]]
    for triangle_list in triangle[1:]:
        tmp_list=[]
        for i,num in enumerate(pre_sum_list):
            left_sum=triangle_list[i]+num
            right_sum=triangle_list[i+1]+num
            if len(tmp_list)>=i+1:
                tmp_list[i]=max(left_sum,tmp_list[i])
            else:
                tmp_list.append(left_sum) 
            tmp_list.append(right_sum)
        pre_sum_list=tmp_list
    pre_sum_list.sort(reverse=True)
    
    return pre_sum_list[0]

# triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# print(dynamic_43105(triangle))

def dynamic_42898(m, n, puddles):
    maps=[[1 for i in range(m)] for i in range(n)]
    for [x,y] in puddles:
        maps[y-1][x-1]=0
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            if i-1<0:
                up=0
            else:
                up=maps[i-1][j]
            if j-1<0:
                left=0
            else:
                left=maps[i][j-1]
            if maps[i][j]==0:
                maps[i][j]=0
            else: 
                maps[i][j]=up+left
    return maps[-1][-1]%(1000000007)
m=4
n=3	
puddles=[[2, 1]]

print(dynamic_42898(m, n, puddles))