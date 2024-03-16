def func(x):
    if x<=-0.5:
        return 0.5
    elif x>-0.5 and x<=0:
        return x+1
    elif x>0 and x<=1:
        return x**2 - 1
    return x-1