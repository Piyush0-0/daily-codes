#multiple operations on a string


def lol(x):
    if len(x)<3:
        return x
    m=x[:3]
    if m[1]=="A":
        n=m[0]&m[2]
    elif m[1]=="B":
        n=m[0]|m[2]
    elif m[1]=="C":
        n=m[0]^m[2]
    return lol(n+m[3:])
a=input()
lol(a)
