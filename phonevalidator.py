n=int(input())
ans=[]
l=[]
for i in range(n):
    num=input()
    l.append(num)
for i in l:
    if len(i)==10:
        
        if not i.isdigit():
            ans.append("NO")
        else :
            if i[0]=="7" or i[0]=="8" or i[0]=="9":
                ans.append("YES")
            else :
                ans.append("NO")
    else :
        ans.append("NO")
for i in ans:
    print(i)