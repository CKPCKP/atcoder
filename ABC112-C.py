n = int(input())
a = [list(map(int, input().split(' '))) for i in range(n)]
for x in range(101):
    for y in range(101):
        for i in range(n):
            if a[i][2] > 0:
                htop = a[i][2] + abs(x-a[i][0]) + abs(y-a[i][1])
                break
        for i in range(n):
            if a[i][2] == 0:
                if htop - (abs(x-a[i][0]) + abs(y-a[i][1])) > 0:
                    break
            if a[i][2] > 0:
                if htop - (abs(x-a[i][0]) + abs(y-a[i][1])) != a[i][2]:
                    break
        else:
            print(x,y,htop)
            exit()