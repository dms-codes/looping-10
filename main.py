n = int(input())
for i in range(0,n+1):
    print(str(i).rjust(2),str('1'+(i*'0')).rjust(n+1))
