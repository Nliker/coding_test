def string_lps(strings,lps):
    leng=0
    i=1
    while i<len(strings):
        if strings[i]==strings[leng]:
            leng+=1
            lps[i]=leng
            i+=1
        else:
            if leng !=0:
                leng=lps[leng-1]
            else:
                lps[i]=0
                i+=1     
    return 
# strings="ABCAB"
# strings="ABCABA"
strings="ABCDWWWABCDRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRABCDWWWABCDW"
lps=[0 for _ in range(len(strings))]
string_lps(strings,lps)
print(lps)

