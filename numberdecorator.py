
def wrapper(f):
    def fun(l):
        ans=[]
        # l.sort()
        for i in l:
            if len(i)>10:
                diff=len(i)-10
                k=i[diff:len(i)]
                ans.append(k)
            elif len(i)==10:
                ans.append(i)
        l.clear()
        for i in ans:
            l.append(i[0:5]+ " " + i[5:10])
            print(i[0:5]+ " " + i[5:10])
        # print(l)    
        for i in l:
            print("+91 "+i)
        return l
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)