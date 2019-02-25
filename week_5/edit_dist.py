def editdistance(a,b):
    x = len(a)
    y = len(b)
    z = [[0]*(y+1) for i in range(x+1)] 
    for i in range(0, x+1):
        z[i][0] = i
    for i in range(0, y+1):
        z[0][i] = i
    move=0
    for i in range(1, x+1):
        for j in range(1, y+1):
            if a[i-1] == b[j-1]:
                move=0
            else:
                move=1
            z[i][j] = min(min(z[i-1][j], z[i][j-1])+1, z[i-1][j-1]+move)
    
    return z[x][y]

a=raw_input()
b=raw_input()
print editdistance(a,b)
