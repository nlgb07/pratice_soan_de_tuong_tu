def rgps(x, y):
    if (x%y == 0):
        return int(x/y)
    
    k = 1
    if (abs(x) > abs(y)):
        for i in range(1, abs(y)+1):
            if (x%i==0 and y%i==0):
                if (i > k):
                    k = i
    else:
        for i in range(1, abs(x)+1):
            if (x%i==0 and y%i==0):
                if (i > k):
                    k = i

    if (x*y < 0):
        return f"$- \\dfrac{{ {abs(int(x/k))} }}{{ {abs(int(y/k))} }} $"
    elif (x*y > 0):
        return f"$ \\dfrac{{ {abs(int(x/k))} }}{{ {abs(int(y/k))} }} $"

print(rgps(8,-2))
#print(abs(-2))